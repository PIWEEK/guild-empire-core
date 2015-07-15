
class GECoreException(Exception):
    '''
    Base class for all exception raised form Game Empires core.
    '''
    pass


class InvalidValue(GECoreException):
    '''
    The user has submitted an invalid value in a turn.
    '''
    pass
