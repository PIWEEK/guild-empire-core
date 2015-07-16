from collections import namedtuple

Character = namedtuple('Character', (
    'slug', # str
    'name', # str
    'archetype', # str
    'avatar_slug', # str
    'skills', # {slug: CharacterSkill}
    'conditions', # {slug: CharacterCondition}
    'turn_round', # int
    'turn_next_action', # int
    'turn_finished', # bool
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
