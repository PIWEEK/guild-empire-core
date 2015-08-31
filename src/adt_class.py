import sys

class ADTClass:
    '''
    A class that behaves like an Abstract Data Type. It does not allow arbitrary modification of
    attributes from outside, but else can only change state via well-defined actions (commands).

    >>> from adt_class import ADTClass

    >>> class Point(ADTClass):
    ...     fields = (
    ...       'x', # int
    ...       'y', # int
    ...     )
    ...     def move_horizontal(self, distance):
    ...         self.x = self.x + distance
    ...     def bad_method(self):
    ...         self.z = 0

    >>> p = Point(x = 10, y = 20)
    >>> p.move_horizontal(5)
    >>> p.x
    15
    >>> p.x = 30
    NotImplementedError
    >>> p.bad_method()
    IndexError
    '''

    fields = ()

    def __init__(self, *args, **kwargs):
        for field in self.fields:
            self.__dict__[field] = kwargs[field]

    def __setattr__(self, name, value):
        if sys._getframe(1).f_locals.get('self') != self:
            raise NotImplementedError('You cannot set attributes from outside the class')
        if not name in self.fields:
            raise IndexError('Attribute {name} not found'.format(name=name))
        self.__dict__[name] = value

