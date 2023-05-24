import os
from utilities.files.json import json_utils
from utilities.files.csv import csv_utils


class Helper:
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    __CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))
    __KEY_POSITION = 'posicion'
    __KEY_NAME = 'nombre'

    players: list

    def __init__(self) -> None:
        self.players = json_utils.read_json(self.__JSON_PATH, 'dt')['jugadores']

    @staticmethod
    def __get_name_and_key_string(player, key:str):
        return f'{player[Helper.__KEY_NAME]} - {player[key]}'

    @staticmethod
    def __get_list_with_name_and_key(players:list, key:str) -> list:
        return [Helper.__get_name_and_key_string(player, key) for player in players]

    # Use cases:

    def get_all_with_name_and_position(self):
        return Helper.__get_list_with_name_and_key(self.players, self.__KEY_POSITION)