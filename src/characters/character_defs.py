from collections import namedtuple

Character = namedtuple('Character', (
    'slug', # str
    'name', # str
    'archetype', # str
    'avatar_slug', # str
    'skills', # CharacterSkill[]
    'conditions', # CharacterCondition[]
))


CharacterSkill = namedtuple('CharacterSkill', (
    'slug', # str
    'name', # str
    'value', # int
    'modifier', # int
))

# Skill values:
# 100 = champion
#  80 = master
#  60 = good
#  40 = poor
#  20 = very bad
#   0 = unable

# Skill modifiers:
# +- 30


CharacterCondition = namedtuple('CharacterCondition', (
    'slug', # str
    'name', # str
    'type', # str
    'description', # str
))
