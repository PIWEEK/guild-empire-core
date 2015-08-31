from adt_class import ADTClass

class Guild(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'color', # str
        'assets', # Asset[]
        'members', # Character[]
    )


class GuildAsset(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'value', # int
    )
