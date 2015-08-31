from adt_class import ADTClass

class Place(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'actions', # Action[]
    )

