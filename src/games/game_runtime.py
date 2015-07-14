from collections import namedtuple

Game = namedtuple('Game', [
    'uuid',  # uuid of the game
    'definition',  # game_defs.Game
    'places',  # Place[]
    'guilds', # Guild[]
])

