from games.game_services import *
from games.game_runtime import *
from storage.methods import save_game

game1 = new_game('default')

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
                        character_slug = 'francesco',
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
        'segismundo': TurnCharacter(
            character_slug = 'segismundo',
            actions = [
            ],
        ),
        'francesco': TurnCharacter(
            character_slug = 'francesco',
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
    },
)

game2 = submit_turn(game1, turn_medici)
game3 = submit_turn(game2, turn_malatesta)

for guild in game3.guilds.values():
    print('\n=== {guild} ==='.format(guild = guild.name))
    for character in guild.members.values():
        print('{character}'.format(character = character.name))
        for asset, amount in character.last_turn.guild_assets.items():
            print('  {asset}({amount})'.format(asset = asset, amount = amount))

# save_game(game3)
print("UUID: {}".format(game3.uuid))
