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
    'last_turn', # CharacterLastTurn
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


CharacterLastTurn = namedtuple('CharacterLastTurn', (
    'guild_assets', # {slug: int}
    'character_skills', # {slug: int}
    'events', # CharacterLastTurnEvent[]
))


CharacterLastTurnEvent = namedtuple('CharacterLastTurnEvent', (
    'message', # str
    'condition_gained_slug', # str (may be None, mutually exclusive with lost)
    'condition_lost_slug', # str (may be None, mutually exclusive wit gained)
))

