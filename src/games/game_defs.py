from adt_class import ADTClass

class Game(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'places', # Place[]
        'free_actions', # Action[]
        'guilds', # Guild[]
    )

