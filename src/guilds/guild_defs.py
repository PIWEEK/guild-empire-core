from collections import namedtuple

Guild = namedtuple('Guild', (
    'slug', # str
    'name', # str
    'assets', # Asset[]
    'members', # Character[]
))


GuildAsset = namedtuple('GuildAsset', (
    'slug', # str
    'name', # str
    'value', # int
))

