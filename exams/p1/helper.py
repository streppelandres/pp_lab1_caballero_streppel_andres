import os
from player.PlayerAdapter import adapt_players
from utilities.files.json import json_utils
#from utilities.files.csv import csv_utils


class Helper:
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    #__CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))

    players: list

    def __init__(self) -> None:
        self.players = adapt_players(json_utils.read_json(self.__JSON_PATH, 'dt')['jugadores'])