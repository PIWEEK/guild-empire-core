from collections import namedtuple

Game = namedtuple('Game', (
    'uuid',  # uuid of the game
    'definition',  # game_defs.Game
    'places',  # {slug: Place}
    'guilds', # {slug: Guild}
    'turns', # {slug: Turn}
))


Turn = namedtuple('Turn', (
    'guild', # Guild
    'characters', # {slug: TurnCharacter}
))


TurnCharacter = namedtuple('TurnCharacter', (
    'character', # str
    'actions', # TurnCharacterAction[]
))


TurnCharacterAction = namedtuple('TurnCharacterAction', (
    'place', # str
    'action', # str
    'target', # TurnCharacterActionTarget
))


TurnCharacterActionTarget = namedtuple('TurnCharacterActionTarget', (
    'guild', # str
    'character', # str
))


TurnProcess = namedtuple('TurnProcess', (
    'global_round', # int
    'guild_characters', # {str: {str: TurnProcessCharacter[]}}
))


TurnProcessCharacter = namedtuple('TurnProcessCharacter', (
    'character_round', # int
    'next_action', # int
    'finished', # bool
))

