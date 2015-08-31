from adt_class import ADTClass

class Game(ADTClass):
    fields = (
        'uuid',  # uuid of the game
        'definition',  # game_defs.Game
        'places',  # {slug: Place}
        'guilds', # {slug: Guild}
        'turns', # {slug: Turn}
        'turn_round', # int
    )

    def clear_turns(self):
        self.turns = {}

    def add_turn(self, turn):
        self.turns[turn.guild_slug] = turn

    def has_all_turns(self):
        return len(self.turns) == len(self.guilds)

    def reset_turn_round(self):
        self.turn_round = 0

    def advance_turn_round(self):
        self.turn_round += 1


class Turn(ADTClass):
    fields = (
        'guild_slug', # str
        'characters', # {slug: TurnCharacter}
    )


class TurnCharacter(ADTClass):
    fields = (
        'character_slug', # str
        'actions', # TurnCharacterAction[]
    )


class TurnCharacterAction(ADTClass):
    fields = (
        'place_slug', # str
        'action_slug', # str
        'target', # TurnCharacterActionTarget
    )


class TurnCharacterActionTarget(ADTClass):
    fields = (
        'guild_slug', # str
        'character_slug', # str
    )

