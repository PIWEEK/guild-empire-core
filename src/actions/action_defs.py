from collections import namedtuple

Action = namedtuple('Action', [
    'slug', # str
    'name', # str
    'action_points', # int
    'skills_needed', # str[]
    'skills_upgraded', # str[]
])

