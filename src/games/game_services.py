import importlib
import sys
import os
from uuid import uuid4

from games import game_runtime
from places import place_defs
from places import place_runtime
from guilds import guild_defs
from guilds import guild_runtime
from characters import character_defs
from characters import character_runtime


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'definitions'))  # adding definitions directory to path


def new_game(slug: str) -> game_runtime.Game:

    # Import a python module with a name equal to the slug, in the 'definitions' directory
    game_def_module = importlib.import_module(slug)
    game_def = getattr(game_def_module, slug)

    places = [_new_place(place_def) for place_def in game_def.places]
    guilds = [_new_guild(guild_def) for guild_def in game_def.guilds]

    return game_runtime.Game(
        uuid = str(uuid4()),
        definition = game_def,
        places = places,
        guilds = guilds,
    )


def _new_place(place_def: place_defs.Place) -> place_runtime.Place:
    return place_runtime.Place(
        definition = place_def,
    )


def _new_guild(guild_def: guild_defs.Guild) -> guild_runtime.Guild:
    assets = [_new_guild_asset(asset_def) for asset_def in guild_def.assets]
    members = [_new_character(character_def) for character_def in guild_def.members]

    return guild_runtime.Guild(
        slug = guild_def.slug,
        name = guild_def.name,
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
    skills = [_new_character_skill(skill_def) for skill_def in character_def.skills]
    conditions = [_new_character_condition(condition_def) for condition_def in character_def.conditions]

    return character_runtime.Character(
        slug = character_def.slug,
        name = character_def.name,
        archetype = character_def.archetype,
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


def get_guild_from_game(game: game_runtime.Game, guild_slug: str) -> guild_runtime.Guild:
    for guild in game.guilds:
        if guild.slug == guild_slug:
            return guild
    return None
