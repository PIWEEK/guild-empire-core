from collections import namedtuple

Place = namedtuple('Place', [
    'slug', # str
    'name', # str
    'actions', # Action[]
])

