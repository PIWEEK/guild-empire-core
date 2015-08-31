from adt_class import ADTClass

class Character(ADTClass):
    fields = (
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
    )

    def reset_turn_finished(self):
        self.turn_finished = False

    def finish_turn(self):
        self.turn_finished = True
        self.turn_round = 0
        self.turn_next_action = 0

    def advance_turn_round(self, action_points):
        self.turn_round += action_points
        self.turn_next_action += 1

    def acquire_condition(self, condition: 'CharacterCondition'):
        self.conditions[condition.slug] = condition

    def drop_condition(self, condition: 'CharacterCondition'):
        del self.conditions[condition.slug]


class CharacterSkill(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'value', # int
        'modifier', # int
    )

    def update_value(self, amount: int):
        self.value += amount


class CharacterCondition(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'type', # str
        'description', # str
    )


class CharacterLastTurn(ADTClass):
    fields = (
        'guild_assets', # {slug: int}
        'character_skills', # {slug: int}
        'events', # CharacterLastTurnEvent[]
    )

    def reset(self):
        self.guild_assets = {}
        self.character_skills = {}
        self.events = []

    def update_asset(self, asset_slug: str, amount: int):
        total = self.guild_assets.get(asset_slug, 0)
        self.guild_assets[asset_slug] = total + amount

    def update_skill(self, skill_slug: str, amount: int):
        total = self.character_skills.get(skill_slug, 0)
        self.character_skills[skill_slug] = total + amount

    def add_event(self, event: 'CharacterLastTurnEvent'):
        self.events.append(event)


class CharacterLastTurnEvent(ADTClass):
    fields = (
        'message', # str
        'condition_gained_slug', # str (may be None, mutually exclusive with lost)
        'condition_lost_slug', # str (may be None, mutually exclusive wit gained)
    )

