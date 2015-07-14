# coding: utf-8

# python
import os
import pickle

# core
from games import game_runtime
from storage.environment import GAMES
from storage import conf


def _get_game_save_path(uuid: str):
    """ Retrieves a path to save a game instance in disk.
    Mostly used to configure the stored filename
    """
    return os.path.join(conf.GAMES_PATH, 'game-{}'.format(uuid))


def load_game(uuid: str) -> game_runtime.Game:
    # Return the in-memory game instance if present
    if uuid in GAMES:
        return GAMES[uuid]

    # Try to load it from disk
    path = _get_game_save_path(uuid)

    if os.path.isfile(path):
        # load game
        handler = open(path, 'rb')
        pickled_game = handler.read()
        handler.close()

        game = pickle.loads(pickled_game)

        _save_game_in_memory(game)

        return game

    raise Exception('Saved game does not exist')


def _save_game_in_memory(game: game_runtime.Game):
    """ Stores game into memory dict
    """
    GAMES[game.uuid] = game


def save_game(game: game_runtime.Game) -> game_runtime.Game:
    _save_game_in_memory(game)

    pickled_game = pickle.dumps(game)

    handler = open(_get_game_save_path(game.uuid), 'wb')
    handler.write(pickled_game)
    handler.close()

    return game
