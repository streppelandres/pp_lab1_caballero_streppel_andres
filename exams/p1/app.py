from utilities.console.console_utils import clear_console, request_input, request_int_in_range, request_string, request_int
from config.parser import load_config
from helper import Helper

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/menu.ini'

class App:
    helper: Helper
    menu: str
    menu_splited: list
    options: dict

    def __init__(self) -> None:
        self.helper = Helper()
        self.menu = load_config(INI_CONFIG_PATH)['MENU']['es']
        self.menu_splited = self.menu.splitlines()
        self.options = {
            '1': self.option_1, '2': self.option_2,
            '3': self.option_3, '4': self.option_4,
            '5': self.option_5, '6': self.option_6,
            '7': self.option_7, '8': self.option_8,
            '9': self.option_9, '10': self.option_10,
            '11': self.option_11, '12': self.option_12,
            'X': self.option_exit
        }

    def start(self):
        while True:
            clear_console()
            option = input(self.menu + '\n').upper()
            if option in self.options:
                self.options[option]()
            else:
                clear_console()
                print('Opción incorrecta, vuelva a intentar\n')
                request_input()

    def __request_player_by_name(self):
        print(''.join([f'{player.name}\n' for player in self.helper.players]))
        return request_string('Ingrese el nombre del jugador a buscar:\n', [p.name for p in self.helper.players], 'Por favor, ingrese un nombre valido:\n')

    def __print_playeres_with_greater_stat_attr_than_value(self, message:str, attr_name:str):
        greater_than = request_int(f'{message}:\n', 'Por favor, ingrese un número válido')
        players = self.helper.get_playeres_with_greater_stat_attr_than_value(attr_name, greater_than)
        if players:
            print(f'Jugadores con {attr_name.replace("_", " ")} mayor a {greater_than}:\n')
            print('\n'.join([f'{player.name} - {getattr(player.statistics, attr_name)}' for player in players]))
        else:
            print(f'No se encontraron jugadores con {attr_name.replace("_", " ")} mayor a {greater_than}\n')

    def option_1(self):
        clear_console()
        print(self.menu_splited[1])
        print(''.join([f'{player.name} - {player.position}\n' for player in self.helper.players]))
        request_input()

    def option_2(self):
        clear_console()
        print(self.menu_splited[2])
        players = [f'{i} - {player.name} - {player.position}\n' for i, player in enumerate(self.helper.players)]
        print(''.join(players))
        player = self.helper.players[request_int_in_range('Ingrese un indice para poder ver sus estadísticas:\n', 0, len(players))]
        clear_console()
        print(player.name)
        print(player.statistics)
        self.helper.save_player_stats_to_csv(player, f'player_stats_{player.name.lower().replace(" ", "_")}')
        request_input()

    def option_3(self):
        clear_console()
        print(self.menu_splited[3])
        print('\n'.join(self.helper.get_player_archivements_by_name(self.__request_player_by_name())))
        request_input()

    def option_4(self):
        clear_console()
        print(self.menu_splited[4])
        print(f'Promedio del equipo: {format(self.helper.get_team_average_point_per_match(), ".2f")}')
        print(''.join([f'{player.name} - {player.statistics.average_points_per_game}\n' for player in sorted(self.helper.players, key = lambda p : p.name)]))
        request_input()

    def option_5(self):
        clear_console()
        print(self.menu_splited[5])
        player_name = self.__request_player_by_name()
        print(f'{player_name.capitalize()} {self.helper.is_hall_of_fame_player_by_name(player_name) and "es" or "no es"} miembro del salón de la fama')
        request_input()

    def option_6(self):
        clear_console()
        print(self.menu_splited[6])
        player = self.helper.get_player_with_max_rebounds()
        print(f'{player.name} - {player.statistics.total_rebounds}\n')
        request_input()

    def option_7(self):
        clear_console()
        print(self.menu_splited[7])
        player = self.helper.get_player_with_max_field_goal_percentage()
        print(f'{player.name} - {player.statistics.field_goal_percentage}\n')
        request_input()

    def option_8(self):
        clear_console()
        print(self.menu_splited[8])
        player = self.helper.get_player_with_max_total_assists()
        print(f'{player.name} - {player.statistics.total_assists}\n')
        request_input()

    def option_9(self):
        clear_console()
        print(self.menu_splited[9])
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de puntos por partido:', 'average_points_per_game')
        request_input()

    def option_10(self):
        clear_console()
        print(self.menu_splited[10])
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de rebotes por partido:', 'average_rebounds_per_game')
        request_input()

    def option_11(self):
        clear_console()
        print(self.menu_splited[11])
        self.__print_playeres_with_greater_stat_attr_than_value('Ingrese un promedio de asistencias por partido:', 'average_assists_per_game')
        request_input()
    
    def option_12(self):
        clear_console()
        print(self.menu_splited[12])
        player = self.helper.get_player_with_max_total_steals()
        print(f'{player.name} - {player.statistics.total_steals}\n')
        request_input()


    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)
