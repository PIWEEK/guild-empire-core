from copy import copy


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
            sub_structure = copy(structure[path_cur])
            sub_value = replace(sub_structure, path_rest, value)

    if isinstance(structure, tuple):
        return structure._replace(**{path_cur: sub_value})
    else:
        structure[path_cur] = sub_value
        return structure

