import exceptions
import utils

from games import game_runtime
from places import place_runtime
from guilds import guild_runtime
from characters import character_runtime
from actions import action_defs


def find_action(action_slug: str, game: game_runtime.Game, place: place_runtime.Place) -> action_defs.Action:
    '''
    Find an action in a game, by slug, and related to some place.
    '''
    action = utils.pick_element(lambda action: action.slug == action_slug, place.definition.actions)
    if not action:
        action = utils.pick_element(lambda action: action.slug == action_slug, game.definition.free_actions)
    return action


def process_action(
        game: game_runtime.Game,
        guild: guild_runtime.Guild,
        character: character_runtime.Character,
        place: place_runtime.Place,
        action: action_defs.Action,
    ):

    updated_game = game

    print('{round}: {character} is doing {action} in {place}'.format(
        round = game.turn_round,
        action = action.name,
        character = character.name,
        place = place.definition.name
    ))

    updated_game = utils.replace(
        updated_game,
        'guilds.' + guild.slug + '.members.' + character.slug + '.turn_round',
        character.turn_round + action.action_points
    )
    updated_game = utils.replace(
        updated_game,
        'guilds.' + guild.slug + '.members.' + character.slug + '.turn_next_action',
        character.turn_next_action + 1,
    )

    return updated_game

