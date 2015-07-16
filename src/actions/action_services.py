import exceptions
import utils
import sys

from games import game_runtime
from places import place_runtime
from guilds import guild_runtime
from characters import character_runtime
from actions import action_defs
from actions import action_runtime


def _get_upgraded_skills_from_action(action: action_defs.Action) -> list:
    skills = [
        success.skill_slug  \
            for check in action.checks \
                for success in check.success if getattr(success, 'skill_slug', False)
    ]

    return skills


def find_action(action_slug: str, game: game_runtime.Game, place: place_runtime.Place) -> action_defs.Action:
    '''
    Find an action in a game, by slug, and related to some place.
    '''
    action = utils.pick_element(lambda action: action.slug == action_slug, place.definition.actions)
    if not action:
        action = utils.pick_element(lambda action: action.slug == action_slug, game.definition.free_actions)
    return action


def process_action(game: game_runtime.Game, context: action_runtime.ActionContext) -> game_runtime.Game:
    updated_game = game

    print('{round}: {character} is doing {action} in {place}'.format(
        round = updated_game.turn_round,
        action = context.action.name,
        character = context.character.name,
        place = context.place.definition.name
    ))

    for check in context.action.checks:
        updated_game = process_check(updated_game, context, check)

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.turn_round',
        context.character.turn_round + context.action.action_points
    )
    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.turn_next_action',
        context.character.turn_next_action + 1,
    )

    return updated_game


# Action checks

def process_check(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    current_module = sys.modules[__name__]
    process_function = getattr(current_module, 'process_check_' + check.__class__.__name__)
    updated_game = process_function(game, context, check)

    return updated_game


def process_check_ActionCheckAutomatic(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    for result in check.success:
        updated_game = process_result(updated_game, context, check, result)

    return updated_game


def process_check_ActionCheckSkill(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_check_ActionCheckTarget(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_check_ActionCheckRandom(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


# Action results

def process_result(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    current_module = sys.modules[__name__]
    process_function = getattr(current_module, 'process_result_' + result.__class__.__name__)
    updated_game = process_function(game, context, check, result)

    return updated_game


def process_result_ActionResultChangeAssetFixed(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultChangeAssetVariable(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultChangeSkillFixed(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultChangeSkillVariable(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultAcquireCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultDropCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultTargetAcquireCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultTargetDropCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultEvent(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game
