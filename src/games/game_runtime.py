from collections import namedtuple

Game = namedtuple('Game', (
    'uuid',  # uuid of the game
    'definition',  # game_defs.Game
    'places',  # Place[]
    'guilds', # Guild[]
    'turns', # Turn[]
))


Turn = namedtuple('Turn', (
    'guild', # Guild
    'characters', # TurnCharacter[]
))


TurnCharacter = namedtuple('TurnCharacter', (
    'character', # str
    'actions', # list
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

