from collections import namedtuple

Character = namedtuple('Character', (
    'slug', # str
    'name', # str
    'archetype', # str
    'archetype_slug', # str
    'skills', # {slug: CharacterSkill}
    'conditions', # {slug: CharacterCondition}
))


CharacterSkill = namedtuple('CharacterSkill', (
    'slug', # str
    'name', # str
    'value', # int
    'modifier', # int
))


CharacterCondition = namedtuple('CharacterCondition', (
    'slug', # str
    'name', # str
    'type', # str
    'description', # str
))
