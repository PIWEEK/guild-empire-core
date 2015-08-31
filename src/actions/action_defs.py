from adt_class import ADTClass

class Action(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'action_points', # int
        'skills_needed', # str[]
        'checks', # ActionCheck[]
    )


    def upgraded_skills(self) -> list:
        '''
        The slugs of skills that be updated if this accion is a success.
        '''
        return [
            success.skill_slug  \
                for check in self.checks \
                    for success in check.success if hasattr(success, 'skill_slug')
        ]


# Action checks

class ActionCheck(ADTClass):
    fields = (
        'success', # ActionResult[]
    )


class ActionCheckAutomatic(ActionCheck):
    fields = ActionCheck.fields + (
    )


class ActionCheckSkill(ActionCheck):
    fields = ActionCheck.fields + (
        'skill_slug', # str
        'difficulty', # int
        'failure', # ActionResult[]
    )


class ActionCheckTarget(ActionCheck):
    fields = ActionCheck.fields + (
        'skill_slug', # str
        'target_skill_slug', # str
        'failure', # ActionResult[]
        'not_found', # ActionResult[]
    )


class ActionCheckRandom(ActionCheck):
    fields = ActionCheck.fields + (
        'probability', # int
        'skill_slug', # str
        'difficulty', # int
        'failure', # ActionResult[]
        'not_happen', # ActionResult[]
    )


# Action results

class ActionResult(ADTClass):
    fields = (
        'min', # int
        'max', # int
    )


class ActionResultChangeAssetFixed(ActionResult):
    fields = ActionResult.fields + (
        'asset_slug', # str
        'amount', # int
    )


class ActionResultChangeAssetVariable(ActionResult):
    fields = ActionResult.fields + (
        'asset_slug', # str
        'multiplier', # int
    )


class ActionResultChangeSkillFixed(ActionResult):
    fields = ActionResult.fields + (
        'skill_slug', # str
        'amount', # int
    )


class ActionResultChangeSkillVariable(ActionResult):
    fields = ActionResult.fields + (
        'skill_slug', # str
        'multiplier', # int
    )


class ActionResultAcquireCondition(ActionResult):
    fields = ActionResult.fields + (
        'message', # str
        'condition', # CharacterCondition
    )


class ActionResultDropCondition(ActionResult):
    fields = ActionResult.fields + (
        'message', # str
        'condition_slug', # str
    )


class ActionResultTargetAcquireCondition(ActionResult):
    fields = ActionResult.fields + (
        'message', # str
        'target_message', # str
        'condition', # CharacterCondition
    )


class ActionResultTargetDropCondition(ActionResult):
    fields = ActionResult.fields + (
        'message', # str
        'target_message', # str
        'condition_slug', # str
    )


class ActionResultEvent(ActionResult):
    fields = ActionResult.fields + (
        'message', # str
    )

