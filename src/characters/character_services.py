from characters import character_runtime


def init_character_rounds(character: character_runtime.Character):
    '''
    Reset any round info to start processing rounds in a new turn.
    '''
    character.reset_turn_finished()
    character.last_turn.reset()

