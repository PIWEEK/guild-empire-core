from collections import namedtuple

Game = namedtuple('Game', (
    'uuid',  # uuid of the game
    'definition',  # game_defs.Game
    'places',  # {slug: Place}
    'guilds', # {slug: Guild}
    'turns', # {slug: Turn}
    'turn_round', # int
))


Turn = namedtuple('Turn', (
    'guild_slug', # str
    'characters', # {slug: TurnCharacter}
))


TurnCharacter = namedtuple('TurnCharacter', (
    'character_slug', # str
    'actions', # TurnCharacterAction[]
))


TurnCharacterAction = namedtuple('TurnCharacterAction', (
    'place_slug', # str
    'action_slug', # str
    'target', # TurnCharacterActionTarget
))


TurnCharacterActionTarget = namedtuple('TurnCharacterActionTarget', (
    'guild_slug', # str
    'character_slug', # str
))

