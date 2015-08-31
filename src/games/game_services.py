import importlib
import sys
import os
from uuid import uuid4

import exceptions
import utils

from games import game_runtime
from places import place_defs
from places import place_runtime
from guilds import guild_defs
from guilds import guild_runtime
from guilds import guild_services
from characters import character_defs
from characters import character_runtime
from actions import action_runtime
from actions import action_services


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'definitions'))  # adding definitions directory to path


def new_game(slug: str) -> game_runtime.Game:
    '''
    Create a new game runtime from a game definition, and persist it.
    '''

    # Import a python module with a name equal to the slug, in the 'definitions' directory
    game_def_module = importlib.import_module(slug)
    game_def = getattr(game_def_module, slug)

    places = {place_def.slug: _new_place(place_def) for place_def in game_def.places}
    guilds = {guild_def.slug: _new_guild(guild_def) for guild_def in game_def.guilds}

    return game_runtime.Game(
        uuid = str(uuid4()),
        definition = game_def,
        places = places,
        guilds = guilds,
        turns = {},
        turn_round = 0,
    )


def _new_place(place_def: place_defs.Place) -> place_runtime.Place:
    return place_runtime.Place(
        definition = place_def,
    )


def _new_guild(guild_def: guild_defs.Guild) -> guild_runtime.Guild:
    assets = {asset_def.slug: _new_guild_asset(asset_def) for asset_def in guild_def.assets}
    members = {character_def.slug: _new_character(character_def) for character_def in guild_def.members}

    return guild_runtime.Guild(
        slug = guild_def.slug,
        name = guild_def.name,
        color = guild_def.color,
        assets = assets,
        members = members,
    )


def _new_guild_asset(asset_def: guild_defs.GuildAsset) -> guild_runtime.GuildAsset:
    return guild_runtime.GuildAsset(
        slug = asset_def.slug,
        name = asset_def.name,
        value = asset_def.value,
    )


def _new_character(character_def: character_defs.Character) -> character_runtime.Character:
    skills = {skill_def.slug: _new_character_skill(skill_def) for skill_def in character_def.skills}
    conditions = {condition_def.slug: _new_character_condition(condition_def) for condition_def in character_def.conditions}

    return character_runtime.Character(
        slug = character_def.slug,
        name = character_def.name,
        archetype = character_def.archetype,
        avatar_slug = character_def.avatar_slug,
        skills = skills,
        conditions = conditions,
        turn_round = 0,
        turn_next_action = 0,
        turn_finished = False,
        last_turn = character_runtime.CharacterLastTurn(
            guild_assets = {},
            character_skills = {},
            events = [],
        )
    )


def _new_character_skill(skill_def: character_defs.CharacterSkill) -> character_runtime.CharacterSkill:
    return character_runtime.CharacterSkill(
        slug = skill_def.slug,
        name = skill_def.name,
        value = skill_def.value,
        modifier = skill_def.modifier,
    )


def _new_character_condition(condition_def: character_defs.CharacterCondition) -> character_runtime.CharacterCondition:
    return character_runtime.CharacterCondition(
        slug = condition_def.slug,
        name = condition_def.name,
        type = condition_def.type,
        description = condition_def.description,
    )


def submit_turn(game: game_runtime.Game, turn: game_runtime.Turn):
    '''
    Submit a turn from one player. If this was the last slacker, and now all players have sent their turns,
    process them and update the game.
    '''
    if not turn.guild_slug in game.guilds:
        raise exceptions.InvalidValue('Not existing guild {slug}'.format(slug = turn.guild_slug))

    if turn.guild_slug in game.turns:
        raise exceptions.InvalidValue('Duplicated turn for guild {slug}'.format(slug = turn.guild_slug))

    game.add_turn(turn)

    if game.has_all_turns():
        _init_game_rounds(game)
        _process_turns(game)
        game.clear_turns()


def _init_game_rounds(game: game_runtime.Game):
    '''
    Reset any round info to start processing rounds in a new turn.
    '''
    game.reset_turn_round()
    for guild in game.guilds.values():
        guild_services.init_guild_rounds(guild)


def _process_turns(game: game_runtime.Game):
    '''
    Process all the turns received from players and return a new game runtime with all actions resolved.
    '''
    while not _game_turn_finished(game):
        _process_round(game)


def _game_turn_finished(game: game_runtime.Game):
    '''
    Check if all characters of all guilds have finished their actions.
    '''
    return all([guild_services.guild_turn_finished(guild) for guild in game.guilds.values()])


def _process_round(game: game_runtime.Game):
    '''
    Process a round of game for all characters.
    '''
    for guild in game.guilds.values():
        for character in guild.members.values():
            if not character.turn_finished:
                _process_round_character(game, guild, character)

    game.advance_turn_round()


def _process_round_character(game: game_runtime.Game, guild: guild_runtime.Guild, character: character_runtime.Character):
    '''
    Process a round of game for one character. If the character has no more actions, set the finished flag.
    '''
    guild_turn = game.turns[guild.slug]
    turn_character = guild_turn.characters.get(character.slug, None)
    turn_actions = turn_character.actions if turn_character else []

    if not turn_actions or character.turn_next_action >= len(turn_actions):
        character.finish_turn()
    else:
        if character.turn_round <= game.turn_round:

            turn_action = turn_actions[character.turn_next_action]
            place = game.places[turn_action.place_slug]
            action = action_services.find_action(turn_action.action_slug, game, place)
            if turn_action.target:
                target_guild = game.guilds[turn_action.target.guild_slug]
                target_character = target_guild.members[turn_action.target.character_slug]
            else:
                target_guild = None
                target_character = None

            context = action_runtime.ActionContext(
                guild = guild,
                character = character,
                place = place,
                action = action,
                target_guild = target_guild,
                target_character = target_character,
            )

            action_services.process_action(game, context)

