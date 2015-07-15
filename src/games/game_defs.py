from collections import namedtuple

Game = namedtuple('Game', (
    'slug', # str
    'name', # str
    'places', # Place[]
    'free_actions', # Action[]
    'guilds', # Guild[]
))


Turn = namedtuple('PlayerTurn', (
    'guild', # Guild
    'characters', # TurnCharacter[]
))


TurnCharacter = namedtuple('PlayerTurnCharacter', (
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
