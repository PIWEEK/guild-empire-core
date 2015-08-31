import exceptions
import utils
import sys

from games import game_runtime
from places import place_runtime
from guilds import guild_runtime
from characters import character_runtime
from actions import action_defs
from actions import action_runtime


def find_action(action_slug: str, game: game_runtime.Game, place: place_runtime.Place) -> action_defs.Action:
    '''
    Find an action in a game, by slug, and related to some place.
    '''
    action = utils.pick_element(lambda action: action.slug == action_slug, place.definition.actions)
    if not action:
        action = utils.pick_element(lambda action: action.slug == action_slug, game.definition.free_actions)
    return action


def process_action(game: game_runtime.Game, context: action_runtime.ActionContext):
    '''
    Process one action within a context, and makes any required modifications in the game state.

    Then increments the turn round indexes of the character as needed.
    '''
    if not context.target_guild:
        print('{round}: {character} {guild} is doing {action} in {place}'.format(
            round = game.turn_round,
            action = context.action.name,
            character = context.character.name,
            guild = context.guild.name,
            place = context.place.definition.name,
        ))
    else:
        print('{round}: {character} {guild} is doing {action} to {target_character} {target_guild} in {place}'.format(
            round = game.turn_round,
            action = context.action.name,
            character = context.character.name,
            guild = context.guild.name,
            place = context.place.definition.name,
            target_character = context.target_character.name,
            target_guild = context.target_guild.name,
        ))

    for check in context.action.checks:
        process_check(context, check)

    context.character.advance_turn_round(context.action.action_points)


# Action checks

def process_check(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ):
    '''
    Process one check of an action, and execute some of the results inside.
    '''
    current_module = sys.modules[__name__]
    process_function = getattr(current_module, 'process_check_' + check.__class__.__name__)
    process_function(context, check)


def process_check_ActionCheckAutomatic(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ):

    print(' (automatic)')
    for result in check.success:
        process_result(context, check, result, 0)


def process_check_ActionCheckSkill(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ):

    skill = context.character.skills[check.skill_slug]
    roll = utils.dice_roll(skill.value + skill.modifier, check.difficulty)

    if roll >= 0:
        print(' (success)')
        for result in check.success:
            process_result(context, check, result, roll)
    else:
        print(' (failure)')
        for result in check.failure:
            process_result(context, check, result, -roll)


def process_check_ActionCheckTarget(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ):

    # TODO
    print(' (skipped)')


def process_check_ActionCheckRandom(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ):

    from random import randint
    if randint(1, 100) <= check.probability:
        skill = context.character.skills[check.skill_slug]
        roll = utils.dice_roll(skill.value + skill.modifier, check.difficulty)

        if roll >= 0:
            print(' (success)')
            for result in check.success:
                process_result(context, check, result, roll)
        else:
            print(' (failure)')
            for result in check.failure:
                process_result(context, check, result, -roll)
    else:
        print(' (not_happen)')
        for result in check.not_happen:
            process_result(context, check, result, 0)



# Action results

def process_result(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):
    '''
    Process one action result, making some modifications on the game status.
    '''
    if (result.min == 0 or roll >= result.min) and (result.max == 0 or roll <= result.max):
        current_module = sys.modules[__name__]
        process_function = getattr(current_module, 'process_result_' + result.__class__.__name__)
        process_function(context, check, result, roll)


def process_result_ActionResultChangeAssetFixed(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    print(' -> {guild} change {asset} by {amount}'.format(
        guild = context.guild.name,
        asset = result.asset_slug,
        amount = result.amount)
    )

    context.guild.assets[result.asset_slug].update_value(result.amount)
    context.character.last_turn.update_asset(result.asset_slug, result.amount)


def process_result_ActionResultChangeAssetVariable(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    amount = roll * result.multiplier

    print(' -> {guild} change {asset} by {amount}'.format(
        guild = context.guild.name,
        asset = result.asset_slug,
        amount = amount)
    )

    context.guild.assets[result.asset_slug].update_value(amount)
    context.character.last_turn.update_asset(result.asset_slug, amount)


def process_result_ActionResultChangeSkillFixed(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    print(' -> {character} change {skill} by {amount}'.format(
        character = context.character.name,
        skill = result.skill_slug,
        amount = result.amount)
    )

    context.character.skills[result.skill_slug].update_value(result.amount)
    context.character.last_turn.update_skill(result.skill_slug, result.amount)


def process_result_ActionResultChangeSkillVariable(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    amount = roll * result.multiplier

    print(' -> {character} change {skill} by {amount}'.format(
        character = context.character.name,
        skill = result.skill_slug,
        amount = amount)
    )

    context.character.skills[result.skill_slug].update_value(amount)
    context.character.last_turn.update_skill(result.skill_slug, amount)


def process_result_ActionResultAcquireCondition(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    message = result.message.format(
        guild = context.guild.name,
        character = context.character.name,
        target_guild = context.target_guild.name if context.target_guild else '',
        target_character = context.target_character.name if context.target_character else '',
    )

    print(' -> {message} [acquire {condition}]'.format(message = message, condition = result.condition.slug))

    context.character.acquire_condition(result.condition)
    context.character.last_turn.add_event(
        character_runtime.CharacterLastTurnEvent(
            message = message,
            condition_gained_slug = result.condition.slug,
            condition_lost_slug = None,
        )
    )


def process_result_ActionResultDropCondition(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    condition = context.character.conditions.get(result.condition_slug, None)

    if condition:
        message = result.message.format(
            guild = context.guild.name,
            character = context.character.name,
            target_guild = context.target_guild.name if context.target_guild else '',
            target_character = context.target_character.name if context.target_character else '',
        )

        print(' -> {message} [drop {condition}]'.format(message = message, condition = condition.slug))

        context.character.drop_condition(condition)
        context.character.last_turn.add_event(
            character_runtime.CharacterLastTurnEvent(
                message = message,
                condition_gained_slug = None,
                condition_lost_slug = condition.slug,
            )
        )


def process_result_ActionResultTargetAcquireCondition(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    if not context.target_guild or not context.target_character:
        raise exceptions.InvalidValue('Action {action} needs target'.format(action = context.action.name))

    message = result.message.format(
        guild = context.guild.name,
        character = context.character.name,
        target_guild = context.target_guild.name,
        target_character = context.target_character.name,
    )

    target_message = result.target_message.format(
        guild = context.guild.name,
        character = context.character.name,
        target_guild = context.target_guild.name,
        target_character = context.target_character.name,
    )

    print(' -> {message} [acquire {condition}]'.format(message = message, condition = result.condition.slug))

    context.target_character.acquire_condition(result.condition)
    context.character.last_turn.add_event(
        character_runtime.CharacterLastTurnEvent(
            message = message,
            condition_gained_slug = None,
            condition_lost_slug = None,
        )
    )
    context.target_character.last_turn.add_event(
        character_runtime.CharacterLastTurnEvent(
            message = target_message,
            condition_gained_slug = result.condition.slug,
            condition_lost_slug = None,
        )
    )


def process_result_ActionResultTargetDropCondition(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    if not context.target_guild or not context.target_character:
        raise exceptions.InvalidValue('Action {action} needs target'.format(action = context.action.name))

    condition = context.target_character.conditions.get(result.condition_slug, None)

    if condition:
        message = result.message.format(
            guild = context.guild.name,
            character = context.character.name,
            target_guild = context.target_guild.name,
            target_character = context.target_character.name,
        )

        target_message = result.target_message.format(
            guild = context.guild.name,
            character = context.character.name,
            target_guild = context.target_guild.name,
            target_character = context.target_character.name,
        )

        print(' -> {message} [drop {condition}]'.format(message = message, condition = result.condition.slug))

        context.target_character.drop_condition(result.condition)
        context.character.last_turn.add_event(
            character_runtime.CharacterLastTurnEvent(
                message = message,
                condition_gained_slug = None,
                condition_lost_slug = None,
            )
        )
        context.target_character.last_turn.add_event(
            character_runtime.CharacterLastTurnEvent(
                message = target_message,
                condition_gained_slug = None,
                condition_lost_slug = result.condition.slug,
            )
        )


def process_result_ActionResultEvent(
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ):

    message = result.message.format(
        guild = context.guild.name,
        character = context.character.name,
        target_guild = context.target_guild.name if context.target_guild else '',
        target_character = context.target_character.name if context.target_character else '',
    )

    print(' -> {message}'.format(message = message))

    context.character.last_turn.add_event(
        character_runtime.CharacterLastTurnEvent(
            message = message,
            condition_gained_slug = None,
            condition_lost_slug = None,
        )
    )

