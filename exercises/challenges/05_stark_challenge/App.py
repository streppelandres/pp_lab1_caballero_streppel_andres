from utils.json_utils import load_json
from utils.config_utils import load_config
from utils.console_utils import *
from HeroesHelper import HeroesHelper

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/config.ini'

class App:
    heroes_helper: HeroesHelper
    menu: str
    options : dict
    
    def __init__(self):
        '''
        Initialize the app, load the heroes data, ini config file and menu options
        '''
        self.heroes_helper = HeroesHelper(load_json(JSON_DATA_PATH))
        self.config = load_config(INI_CONFIG_PATH)
        self.options = {
            'A' : self.option_a,
            'B' : self.option_b,
            'C' : self.option_c,
            'D' : self.option_d,
            'E' : self.option_e,
            'F' : self.option_f,
            'G' : self.option_g,
            'H' : self.option_h,
            'X' : self.option_exit
        }


    def start(self):
        while True:
            clear_console()
            option = input(self.config['TEXT']['menu'] + '\n').upper()
            if option in self.options:
                self.options[option]()
            else:
                clear_console()
                print('Opción incorrecta, vuelva a intentar\n')
                request_input()


    @staticmethod
    def print_heroes(heroes, hide_identities=True):
        for hero in heroes:
            App.print_hero(hero, hide_identities)

    @staticmethod
    def print_heroes_with_attr(heroes, attr, hide_identities=True):
        for hero in heroes:
            App.print_hero_with_attr(hero, attr, hide_identities)

    @staticmethod
    def print_hero(hero, hide_identity=True):
        print(hero.get_name(hide_identity))
    
    @staticmethod
    def print_hero_with_attr(hero, attr, hide_identity=True):
        print(hero.get_name_and_attr(attr, hide_identity))

    def option_a(self):
        clear_console()
        print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M:\n')
        App.print_heroes(self.heroes_helper.get_males_heroes())
        request_input()
    

    def option_b(self):
        clear_console()
        print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F:\n')
        App.print_heroes(self.heroes_helper.get_females_heroes())
        request_input()


    def option_c(self):
        clear_console()
        print('Recorrer la lista y determinar cuál es el superhéroe más alto de género M:\n')
        print(self.heroes_helper.get_more_height_male())
        request_input()

    def option_d(self):
        clear_console()
        print('Recorrer la lista y determinar cuál es el superhéroe más alto de género F :\n')
        print(self.heroes_helper.get_more_height_female())
        request_input()

    def option_e(self):
        clear_console()
        print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:\n')
        print(self.heroes_helper.get_less_height_male())
        request_input()

    def option_f(self):
        clear_console()
        print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:\n')
        print(self.heroes_helper.get_less_height_female())
        request_input()
    
    def option_g(self):
        clear_console()
        print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género M:\n')
        print(self.heroes_helper.get_average_height_male())
        request_input()

    def option_h(self):
        clear_console()
        print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género F:\n')
        print(self.heroes_helper.get_average_height_female())
        request_input()

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)