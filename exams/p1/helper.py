import os
from player.PlayerAdapter import adapt_players
from player.Player import Player
from utilities.files.json import json_utils
from utilities.files.csv import csv_utils


class Helper:
    __JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_data'))
    __CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './_tmp'))
    __HALL_FAME_MEMBER_ARCHIVEMENT = 'Miembro del Salon de la Fama del Baloncesto'

    players: list

    def __init__(self) -> None:
        self.players = adapt_players(json_utils.read_json(self.__JSON_PATH, 'dt')['jugadores'])

    def save_player_stats_to_csv(self, player:Player, file_name:str) -> bool:
        csv_head = ['name', 'position', 'seasons', 'total_points', 'average_points_per_game', 'total_rebounds',
                    'average_rebounds_per_game', 'total_assists', 'average_assists_per_game', 'total_steals',
                    'total_blocks', 'field_goal_percentage', 'free_throw_percentage', 'three_point_percentage']
        ps = player.statistics
        csv_body = [player.name, player.position, ps.seasons, ps.total_points, ps.average_points_per_game, ps.total_rebounds,
                    ps.average_rebounds_per_game, ps.total_assists, ps.average_assists_per_game, ps.total_steals, ps.total_blocks,
                    ps.field_goal_percentage, ps.free_throw_percentage, ps.three_point_percentage]
        csv_utils.save_csv(self.__CSV_PATH, file_name, [csv_head] + [csv_body])
    
    def get_team_average_point_per_match(self) -> float:
        return sum([player.statistics.average_points_per_game for player in self.players]) / len(self.players)
    
    def get_player_archivements_by_name(self, player_name:str) -> list:
        return list(filter(lambda p : p.name.lower() == str(player_name).lower(), self.players))[0].archivements
    
    def is_hall_of_fame_player_by_name(self, player_name:str) -> bool:
        return Helper.__HALL_FAME_MEMBER_ARCHIVEMENT in self.get_player_archivements_by_name(player_name)

    def __get_player_with_max_stat_attr(self, attr_name:str) -> Player:
        return max(self.players, key = lambda player : getattr(player.statistics, attr_name))

    def get_player_with_max_rebounds(self) -> Player:
        return self.__get_player_with_max_stat_attr('total_rebounds')
    
    def get_player_with_max_field_goal_percentage(self) -> Player:
        return self.__get_player_with_max_stat_attr('field_goal_percentage')
    
    def get_player_with_max_total_assists(self) -> Player:
        return self.__get_player_with_max_stat_attr('total_assists')
    
    
