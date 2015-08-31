from adt_class import ADTClass

class Guild(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'color', # str
        'assets', # {slug: Asset}
        'members', # {slug: Character}
    )


class GuildAsset(ADTClass):
    fields = (
        'slug', # str
        'name', # str
        'value', # int
    )

    def update_value(self, amount: int):
        self.value += amount

