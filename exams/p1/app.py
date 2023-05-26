from utilities.console.console_utils import clear_console, request_input, request_int_in_range, print_elements_in_str, print_json
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
            '3': self.option_3, 'X': self.option_exit
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
        request_input()

    def option_3(self):
        clear_console()
        print(self.menu_splited[3])
        request_input()

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)
