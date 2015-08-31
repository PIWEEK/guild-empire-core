from adt_class import ADTClass

class ActionContext(ADTClass):
    fields = (
        'guild', # guild_runtime.Guild,
        'character', # character_runtime.Character,
        'place', # place_runtime.Place,
        'action', # action_defs.Action,
        'target_guild', # guild_runtime.Guild (may be None),
        'target_character', # character_runtime.Character (may be None),
    )

