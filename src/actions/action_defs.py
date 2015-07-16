from collections import namedtuple

Action = namedtuple('Action', (
    'slug', # str
    'name', # str
    'action_points', # int
    'skills_needed', # str[]
    'checks', # ActionCheck[]
))


# Action checks

ActionCheck = namedtuple('ActionCheck', (
    'success', # ActionResult[]
))


ActionCheckAutomatic = namedtuple('ActionCheckAutomatic', ActionCheck._fields + (
))


ActionCheckSkill = namedtuple('ActionCheckSkill', ActionCheck._fields + (
    'skill_slug', # str
    'difficulty', # int
    'failure', # ActionResult[]
))


ActionCheckTarget = namedtuple('ActionCheckTarget', ActionCheck._fields + (
    'skill_slug', # str
    'target_skill_slug', # str
    'failure', # ActionResult[]
    'not_found', # ActionResult[]
))


ActionCheckRandom = namedtuple('ActionCheckRandom', ActionCheck._fields + (
    'probability', # int
    'skill_slug', # str
    'difficulty', # int
    'failure', # ActionResult[]
    'not_happen', # ActionResult[]
))


# Action results

ActionResult = namedtuple('ActionResult', (
    'min', # int
    'max', # int
))


ActionResultChangeAssetFixed = namedtuple('ActionResultChangeAssetFixed', ActionResult._fields + (
    'asset_slug', # str
    'amount', # int
))


ActionResultChangeAssetVariable = namedtuple('ActionResultChangeAssetVariable', ActionResult._fields + (
    'asset_slug', # str
    'multiplier', # int
))


ActionResultChangeSkillFixed = namedtuple('ActionResultChangeSkillFixed', ActionResult._fields + (
    'skill_slug', # str
    'amount', # int
))


ActionResultChangeSkillVariable = namedtuple('ActionResultChangeSkillVariable', ActionResult._fields + (
    'skill_slug', # str
    'multiplier', # int
))


ActionResultAcquireCondition = namedtuple('ActionResultAcquireCondition', ActionResult._fields + (
    'message', # str
    'condition', # CharacterCondition
))


ActionResultDropCondition = namedtuple('ActionResultDropCondition', ActionResult._fields + (
    'message', # str
    'condition_slug', # str
))


ActionResultTargetAcquireCondition = namedtuple('ActionResultTargetAcquireCondition', ActionResult._fields + (
    'message', # str
    'condition', # CharacterCondition
))


ActionResultTargetDropCondition = namedtuple('ActionResultTargetDropCondition', ActionResult._fields + (
    'message', # str
    'condition_slug', # str
))


ActionResultEvent = namedtuple('ActionResultEvent', ActionResult._fields + (
    'message', # str
))
