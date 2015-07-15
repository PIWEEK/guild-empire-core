from collections import namedtuple

Guild = namedtuple('Guild', (
    'slug', # str
    'name', # str
    'color', # str
    'assets', # Asset[]
    'members', # Character[]
))


GuildAsset = namedtuple('GuildAsset', (
    'slug', # str
    'name', # str
    'value', # int
))
