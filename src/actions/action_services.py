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
    '''
    Process one action within a context, and makes any required modifications in the game state.

    Then increments the turn round indexes of the character as needed.
    '''
    updated_game = game

    print('{round}: {character} {guild} is doing {action} in {place}'.format(
        round = updated_game.turn_round,
        action = context.action.name,
        character = context.character.name,
        guild = context.guild.name,
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
    '''
    Process one check of an action, and execute some of the results inside.
    '''
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

    print(' (automatic)')
    for result in check.success:
        updated_game = process_result(updated_game, context, check, result, 0)

    return updated_game


def process_check_ActionCheckSkill(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    skill = context.character.skills[check.skill_slug]
    roll = utils.dice_roll(skill.value + skill.modifier, check.difficulty)

    if roll >= 0:
        print(' (success)')
        for result in check.success:
            updated_game = process_result(updated_game, context, check, result, roll)
    else:
        print(' (failure)')
        for result in check.failure:
            updated_game = process_result(updated_game, context, check, result, -roll)

    return updated_game


def process_check_ActionCheckTarget(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    # TODO

    return updated_game


def process_check_ActionCheckRandom(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
    ) -> game_runtime.Game:

    updated_game = game

    from random import randint
    if randint(1, 100) <= check.probability:
        skill = context.character.skills[check.skill_slug]
        roll = utils.dice_roll(skill.value + skill.modifier, check.difficulty)

        if roll >= 0:
            print(' (success)')
            for result in check.success:
                updated_game = process_result(updated_game, context, check, result, roll)
        else:
            print(' (failure)')
            for result in check.failure:
                updated_game = process_result(updated_game, context, check, result, -roll)
    else:
        print(' (not_happen)')
        for result in check.not_happen:
            updated_game = process_result(updated_game, context, check, result, 0)

    return updated_game



# Action results

def process_result(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:
    '''
    Process one action result, making some modifications on the game status.
    '''
    updated_game = game

    if (result.min == 0 or roll >= result.min) and (result.max == 0 or roll <= result.max):
        current_module = sys.modules[__name__]
        process_function = getattr(current_module, 'process_result_' + result.__class__.__name__)
        updated_game = process_function(updated_game, context, check, result, roll)

    return updated_game


def process_result_ActionResultChangeAssetFixed(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    print(' -> {guild} change {asset} by {amount}'.format(
        guild = context.guild.name,
        asset = result.asset_slug,
        amount = result.amount)
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.assets.' + result.asset_slug + '.value',
        updated_game.guilds[context.guild.slug].assets[result.asset_slug].value + result.amount,
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.last_turn.guild_assets.' + result.asset_slug,
        updated_game.guilds[context.guild.slug].members[context.character.slug].last_turn.guild_assets.get(result.asset_slug, 0) + result.amount,
    )

    return updated_game


def process_result_ActionResultChangeAssetVariable(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    amount = roll * result.multiplier

    print(' -> {guild} change {asset} by {amount}'.format(
        guild = context.guild.name,
        asset = result.asset_slug,
        amount = amount)
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.assets.' + result.asset_slug + '.value',
        updated_game.guilds[context.guild.slug].assets[result.asset_slug].value + amount,
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.last_turn.guild_assets.' + result.asset_slug,
        updated_game.guilds[context.guild.slug].members[context.character.slug].last_turn.guild_assets.get(result.asset_slug, 0) + amount,
    )

    return updated_game


def process_result_ActionResultChangeSkillFixed(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    print(' -> {character} change {skill} by {amount}'.format(
        character = context.character.name,
        skill = result.skill_slug,
        amount = result.amount)
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.skills.' + result.skill_slug + '.value',
        updated_game.guilds[context.guild.slug].members[context.character.slug].skills[result.skill_slug].value + result.amount,
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.last_turn.character_skills.' + result.skill_slug,
        updated_game.guilds[context.guild.slug].members[context.character.slug].last_turn.character_skills.get(result.skill_slug, 0) + result.amount,
    )

    return updated_game


def process_result_ActionResultChangeSkillVariable(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    amount = roll * result.multiplier

    print(' -> {character} change {skill} by {amount}'.format(
        character = context.character.name,
        skill = result.skill_slug,
        amount = amount)
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.skills.' + result.skill_slug + '.value',
        updated_game.guilds[context.guild.slug].members[context.character.slug].skills[result.skill_slug].value + amount,
    )

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.last_turn.character_skills.' + result.skill_slug,
        updated_game.guilds[context.guild.slug].members[context.character.slug].last_turn.character_skills.get(result.skill_slug, 0) + amount,
    )

    return updated_game


def process_result_ActionResultAcquireCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultDropCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultTargetAcquireCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultTargetDropCondition(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    return updated_game


def process_result_ActionResultEvent(
        game: game_runtime.Game,
        context: action_runtime.ActionContext,
        check: action_defs.ActionCheck,
        result: action_defs.ActionResult,
        roll: int,
    ) -> game_runtime.Game:

    updated_game = game

    message = result.message.format(
        guild = context.guild.name,
        character = context.character.name,
        target_guild = context.target_guild.name if context.target_guild else '',
        target_character = context.target_character.name if context.target_character else '',
    )

    print(' -> {message}'.format(message = message))

    updated_game = utils.replace(
        updated_game,
        'guilds.' + context.guild.slug + '.members.' + context.character.slug + '.last_turn.events',
        updated_game.guilds[context.guild.slug].members[context.character.slug].last_turn.events + [
            character_runtime.CharacterLastTurnEvent(
                message = message,
                condition_gained_slug = None,
                condition_lost_slug = None,
            )
        ],
    )

    return updated_game

