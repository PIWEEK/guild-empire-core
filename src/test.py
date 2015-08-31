from games.game_services import *
from games.game_runtime import *
from storage.methods import save_game

game = new_game('default')

turn_medici = Turn(
    guild_slug = 'medici',
    characters = {
        'lorenzo': TurnCharacter(
            character_slug = 'lorenzo',
            actions = [
                TurnCharacterAction(
                    place_slug = 'church',
                    action_slug = 'pray',
                    target = None,
                ),
                TurnCharacterAction(
                    place_slug = 'church',
                    action_slug = 'donate-money',
                    target = None,
                ),
                TurnCharacterAction(
                    place_slug = 'church',
                    action_slug = 'threaten',
                    target = TurnCharacterActionTarget(
                        guild_slug = 'malatesta',
                        character_slug = 'ludovica',
                    ),
                ),
            ],
        ),
        'leonardo': TurnCharacter(
            character_slug = 'lorenzo',
            actions = [
                TurnCharacterAction(
                    place_slug = 'forest',
                    action_slug = 'work-on-woodcutter',
                    target = None,
                ),
                TurnCharacterAction(
                    place_slug = 'forest',
                    action_slug = 'get-wood-near-forest',
                    target = None,
                ),
            ],
        ),
    },
)
turn_malatesta = Turn(
    guild_slug = 'malatesta',
    characters = {
        'vergo': TurnCharacter(
            character_slug = 'vergo',
            actions = [
                TurnCharacterAction(
                    place_slug = 'tavern',
                    action_slug = 'drunk-fighting-tournament',
                    target = None,
                ),
            ],
        ),
        'ludovica': TurnCharacter(
            character_slug = 'ludovica',
            actions = [
                TurnCharacterAction(
                    place_slug = 'forest',
                    action_slug = 'get-wood-near-forest',
                    target = None,
                ),
                TurnCharacterAction(
                    place_slug = 'forest',
                    action_slug = 'get-wood-far-forest',
                    target = None,
                ),
            ],
        ),
        'valerio': TurnCharacter(
            character_slug = 'valerio',
            actions = [
                TurnCharacterAction(
                    place_slug = 'tavern',
                    action_slug = 'get-a-drink',
                    target = None,
                ),
            ],
        ),
    },
)

submit_turn(game, turn_medici)
submit_turn(game, turn_malatesta)

for guild in game.guilds.values():
    print('\n=== {guild} ==='.format(guild = guild.name))
    for character in guild.members.values():
        print('{character}'.format(character = character.name))
        for asset, amount in character.last_turn.guild_assets.items():
            print('  {asset}({amount})'.format(asset = asset, amount = amount))
        for skill, amount in character.last_turn.character_skills.items():
            print('  {skill}({amount})'.format(skill = skill, amount = amount))
        for event in character.last_turn.events:
            if event.condition_gained_slug:
                print('  {message} [+{condition}]'.format(message = event.message, condition = event.condition_gained_slug))
            elif event.condition_lost_slug:
                print('  {message} [-{condition}]'.format(message = event.message, condition = event.condition_lost_slug))
            else:
                print('  {message}'.format(message = event.message))

# save_game(game)
print("UUID: {}".format(game.uuid))
