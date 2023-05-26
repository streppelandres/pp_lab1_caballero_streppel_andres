from utilities.console.console_utils import clear_console, request_input, request_int_in_range, print_elements_in_str, print_json, request_string
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
        print(''.join([f'{player.name}\n' for player in self.helper.players]))
        player_name = request_string('Ingrese el nombre del jugador a buscar:\n', [p.name for p in self.helper.players], 'Por favor, ingrese un nombre valido:\n')
        print('\n'.join(list(filter(lambda p : p.name.lower() == player_name.lower(), self.helper.players))[0].archivements))
        request_input()

    def option_4(self):
        clear_console()
        print(self.menu_splited[4])
        print(f'Promedio del equipo: {format(self.helper.get_team_average_point_per_match(), ".2f")}')
        print(''.join([f'{player.name} - {player.statistics.average_points_per_game}\n' for player in sorted(self.helper.players, key = lambda p : p.name)]))
        request_input()


    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)
