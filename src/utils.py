from copy import copy
from random import randint


def pick_element(function, iterable):
    '''
    Return the first element of the iterable for which function returns True, or None.
    '''
    filtered = filter(function, iterable)
    try:
        return next(filtered)
    except StopIteration:
        return None


def dice_roll(level: int, difficulty: int) -> int:
    '''
    The basic dice roll in this game:
     - Roll 10d10
     - Add level
     - Compare with difficulty

    The result is the difference (success if >= 0, else failure)
    '''
    roll = sum([randint(1, 10) for i in range(10)])
    return (roll + level - difficulty)

