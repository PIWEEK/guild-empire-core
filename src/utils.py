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


def replace(structure, path, value):
    path_list = path.split('.')
    path_cur = path_list[0]
    path_rest = '.'.join(path_list[1:])

    if not path_rest:
        sub_structure = structure
        sub_value = value
    else:
        if isinstance(structure, tuple):
            sub_structure = getattr(structure, path_cur)
            sub_value = replace(sub_structure, path_rest, value)
        else:
            sub_structure = structure[path_cur]
            sub_value = replace(sub_structure, path_rest, value)

    if isinstance(structure, tuple):
        return structure._replace(**{path_cur: sub_value})
    else:
        new_structure = copy(structure)
        new_structure[path_cur] = sub_value
        return new_structure


def updated_dict(dictionary, key, value):
    '''
    Return a new dictionary that is a copy of the original, with the value added in the key.
    '''
    new_dict = copy(dictionary)
    new_dict[key] = value
    return new_dict


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

