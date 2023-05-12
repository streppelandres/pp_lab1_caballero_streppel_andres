from utils.json_utils import load_json
from utils.config_utils import load_config
from utils.console_utils import *
from HeroesHelper import HeroesHelper

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/config.ini'


class App:
    heroes_helper: HeroesHelper
    menu: str
    menu_splited: list
    options: dict

    def __init__(self):
        '''
        Initialize the app, load the heroes data, ini config file and menu options
        '''
        self.heroes_helper = HeroesHelper(load_json(JSON_DATA_PATH))
        self.config = load_config(INI_CONFIG_PATH)
        self.menu = self.config['TEXT']['menu']
        self.menu_splited = self.menu.splitlines()

        # if these was wrapped in classes, maybe this can be done in a dynamic wave
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
        print_json(self.heroes_helper.sort_by_height())
        request_input()

    def option_2(self):
        clear_console()
        print(self.menu_splited[2])
        print_json(self.heroes_helper.sort_by_weight())
        request_input()

    def option_3(self):
        clear_console()
        print(self.menu_splited[3])
        print_json(self.heroes_helper.sort_by_name())
        request_input()

    def option_4(self):
        clear_console()
        print(self.menu_splited[4])
        print_json(self.heroes_helper.sort_by_name_length())
        request_input()

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)
