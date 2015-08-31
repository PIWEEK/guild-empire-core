from guilds import guild_runtime
from characters import character_services


def init_guild_rounds(guild: guild_runtime.Guild):
    '''
    Reset any round info to start processing rounds in a new turn.
    '''
    for character in guild.members.values():
        character_services.init_character_rounds(character)


def guild_turn_finished(guild: guild_runtime.Guild):
    '''
    Check if all characters of this guild have finished their actions.
    '''
    return all([character.turn_finished for character in guild.members.values()])

