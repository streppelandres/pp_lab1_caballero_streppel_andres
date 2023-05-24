import os
from model import Player
from adapter.PlayerAdapter import adapt_players
from utilities.files.json import json_utils
from utilities.files.csv import csv_utils


class Helper:
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    __CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))

    players: list(Player)

    def __init__(self) -> None:
        self.players = adapt_players(json_utils.read_json(self.__JSON_PATH, 'dt')['jugadores'])


    @staticmethod
    def __get_name_and_key_string(player, key:str, index:int, show_index:bool):
        return f'{(not show_index and "-" or index)} {player[Helper.__KEY_NAME]} - {player[key]}'

    @staticmethod
    def __get_list_with_name_and_key(players:list, key:str, show_index:bool=False) -> list:
        return [(Helper.__get_name_and_key_string(player, key, i, show_index)) for i, player in enumerate(players)]
    
    @staticmethod
    def __get_name_and_statistics(player):
        pass

    # Use cases:

    def get_all_with_name_and_position(self):
        return Helper.__get_list_with_name_and_key(self.players,self.__KEY_POSITION)
    
    def get_all_with_name_and_position_with_index(self):
        return Helper.__get_list_with_name_and_key(self.players,self.__KEY_POSITION, True)
    
    def get_player_with_statistics_by_index(self):
        pass