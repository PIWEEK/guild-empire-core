import sys
import os
import importlib

from games import game_defs
from games import game_runtime
from places import place_defs
from places import place_runtime


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'definitions'))  # adding definitions directory to path


def new_game(slug: str) -> game_runtime.Game:

    # Import a python module with a name equal to the slug, in the 'definitions' directory
    game_def_module = importlib.import_module(slug)
    game_def = getattr(game_def_module, slug)

    places = [new_place(place_def) for place_def in game_def.places]

    return game_runtime.Game(
        definition = game_def,
        places = places,
    )


def new_place(place_def: place_defs.Place) -> place_runtime.Place:
    return place_runtime.Place(
        definition = place_def,
    )

