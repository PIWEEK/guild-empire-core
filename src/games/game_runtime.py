from collections import namedtuple

Game = namedtuple('Game', (
    'uuid',  # uuid of the game
    'definition',  # game_defs.Game
    'places',  # Place[]
    'guilds', # Guild[]
))


Turn = namedtuple('Turn', (
    'guild', # Guild
    'characters', # TurnCharacter[]
))


TurnCharacter = namedtuple('TurnCharacter', (
    'character', # Character
    'actions', # TurnCharacterAction[]
))


TurnCharacterAction = namedtuple('TurnCharacterAction', (
    'place', # Place
    'action', # Action,
    'target', # TurnCharacterActionTarget
))


TurnCharacterActionTarget = namedtuple('TurnCharacterActionTarget', (
    'guild', # Guild
    'character', # Character
))

