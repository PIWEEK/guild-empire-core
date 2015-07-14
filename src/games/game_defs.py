from collections import namedtuple

Game = namedtuple('Game', [
    'slug', # str
    'name', # str
    'places', # Place[]
    'free_actions', # Action[]
    'guilds', # Guild[]
])

