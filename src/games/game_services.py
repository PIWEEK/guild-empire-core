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
from characters import character_defs
from characters import character_runtime


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
        archetype_slug = character_def.archetype_slug,
        skills = skills,
        conditions = conditions,
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


def submit_turn(game: game_runtime.Game, turn: game_runtime.Turn) -> game_runtime.Game:
    '''
    Submit a turn from one player. If this was the last slacker, and now all players have sent their turns,
    process them and update the game.
    '''

    if not turn.guild.slug in game.guilds:
        raise exceptions.InvalidValue('Not existing guild {name}'.format(name = turn.guild.name))

    if turn.guild.slug in game.turns:
        raise exceptions.InvalidValue('Duplicated turn for guild {name}'.format(name = turn.guild.name))

    updated_game = utils.replace(game, 'turns', utils.updated_dict(game.turns, turn.guild.slug, turn))

    if len(updated_game.turns) == len(updated_game.guilds):
        updated_game = _process_turns(game)

    return updated_game


def _process_turns(game: game_runtime.Game) -> game_runtime.Game:
    '''
    Process all the turns received from players and return a new game runtime with all actions resolved.
    '''
    # Initialize processing status
    turn_process = game_runtime.TurnProcess(
        global_round = 0,
        guild_characters = {
            guild.slug: {
                member.slug: game_runtime.TurnProcessCharacter(character_round = 0, next_action = 0, finished = False)
                for member in guild.members.values()
            }
            for guild in game.guilds.values()
        }
    )

    # Repeat until all character have exhausted all their actions
    updated_game = game
    while any([any([not character.finished for character in characters.values()]) for characters in turn_process.guild_characters.values()]):
        updated_game, turn_process = _process_round(updated_game, turn_process)

    return updated_game


def _process_round(game: game_runtime.Game, turn_process: game_runtime.TurnProcess) -> (game_runtime.Game, game_runtime.TurnProcess):
    '''
    Process a round of game for all characters.
    '''
    updated_game = game
    updated_turn_process = turn_process

    for guild in game.guilds.values():
        for character in guild.members.values():
            updated_game, updated_turn_process = _process_round_character(game, guild, character, turn_process)

    updated_turn_process = utils.replace(updated_turn_process, 'global_round', updated_turn_process.global_round + 1)

    return updated_game, updated_turn_process


def _process_round_character(
        game: game_runtime.Game,
        guild: guild_runtime.Guild,
        character: character_runtime.Character,
        turn_process: game_runtime.TurnProcess
    ) -> (game_runtime.Game, game_runtime.TurnProcess):
    '''
    Process a round of game for one character. If the character has no more actions, set the finished flag.
    '''
    updated_game = game
    updated_turn_process = turn_process

    guild_turn = game.turns.get(guild.slug, None)
    turn_character = guild_turn.characters.get(character.slug, None) if guild_turn else None
    character_actions = turn_character.actions if turn_character else []

    if not character_actions:
        updated_turn_process = utils.replace(
            updated_turn_process,
            'guild_characters.{guild}.{character}.finished'.format(guild = guild.slug, character = character.slug),
            True
        )

    return updated_game, updated_turn_process

