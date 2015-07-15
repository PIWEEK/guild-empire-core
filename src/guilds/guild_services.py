# coding: utf-8

# core
from characters import character_runtime

# guilds
from guilds import guild_runtime


def get_character_from_guild(guild: guild_runtime.Guild, character_slug: str) -> character_runtime.Character:
    """ Extracts a character namedtuple from a guild based on the character slug
    """
    for character in guild.members:
        if character.slug == character_slug:
            return character
    return None
