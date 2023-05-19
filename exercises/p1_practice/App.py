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
            '5': self.option_5, 'X': self.option_exit
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

    def option_1(self):
        clear_console()
        print(self.menu_splited[1])
        quantity = request_int('Ingrese la cantidad a mostrar:\n')
        heroes = self.heroes_helper.get_by_quantity(quantity)
        if heroes:
            print_elements_in_str(heroes)
            HeroesHelper.save_heroes_to_csv(f'1_list_{quantity}_heroes', heroes)
        else:
            print('No hay heroes para mostrar')
        request_input()
    
    def option_2(self):
        clear_console()
        print(self.menu_splited[2])
        ascending = request_string('Ingrese el orden a mostrar (ASC/DESC):\n', ['asc', 'desc']) == 'asc'
        heroes = self.heroes_helper.sort_by_height(ascending)
        print_elements_in_str(heroes)
        HeroesHelper.save_heroes_to_csv(f'2_list_sorted_by_height', heroes)
        request_input()

    def option_3(self):
        clear_console()
        print(self.menu_splited[3])
        ascending = request_string('Ingrese el orden a mostrar (ASC/DESC):\n', ['asc', 'desc']) == 'asc'
        heroes = self.heroes_helper.sort_by_strength(ascending)
        print_elements_in_str(heroes)
        HeroesHelper.save_heroes_to_csv(f'3_list_sorted_by_strength', heroes)
        request_input()

    def option_4(self):
        clear_console()
        print(self.menu_splited[3])
        
        # FIXME: Mucha repetición, ta bien que sean metodos diferentes, pero hacete algo mas abstracto, mostro
        higher = request_string('Ingrese la condición a mostrar (menor/mayor):\n', ['menor', 'mayor']) == 'mayor'
        higher_txt = higher and 'mayor' or 'menor'
        
        # Height
        height_average = self.heroes_helper.get_height_average()
        height_heroes = self.heroes_helper.filter_height_by_average(height_average, higher)
        print(f'Heroes {higher_txt} al promedio [{height_average}] de altura:')
        print_elements_in_str(height_heroes)
        HeroesHelper.save_heroes_to_csv(f'4_{higher_txt}_average_{height_average}_height', height_heroes)

        # Weight
        weight_average = self.heroes_helper.get_weight_average()
        weight_heroes = self.heroes_helper.filter_weight_by_average(weight_average, higher)
        print(f'Heroes {higher_txt} al promedio [{weight_average}] de peso:')
        print_elements_in_str(weight_heroes)
        HeroesHelper.save_heroes_to_csv(f'4_{higher_txt}_average_{weight_average}_weight', weight_heroes)

        # Strength
        strength_average = self.heroes_helper.get_strength_average()
        strength_heroes = self.heroes_helper.filter_strength_by_average(strength_average, higher)
        print(f'Heroes {higher_txt} al promedio [{strength_average}] de fuerza:')
        print_elements_in_str(strength_heroes)
        HeroesHelper.save_heroes_to_csv(f'4_{higher_txt}_average_{strength_average}_strength', strength_heroes)

        request_input()

    def option_5(self):
        clear_console()
        print(self.menu_splited[3])
        
        valid_intelligences = ['good', 'average', 'high']
        intelligence = request_string(f'Seleccione la inteligencia a buscar ({valid_intelligences}):\n', valid_intelligences)
        heroes = self.heroes_helper.filter_by_intelligence(intelligence)
        print_elements_in_str(heroes)
        HeroesHelper.save_heroes_to_csv(f'5_heroes_with_{intelligence}_intelligence', heroes)

        request_input()

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)