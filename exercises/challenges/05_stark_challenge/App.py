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

        # if these was wrapped in classes, maybe this can be done in a dynamic wave
        self.options = {
            'A' : self.option_a, 'B' : self.option_b, 'C' : self.option_c,
            'D' : self.option_d, 'E' : self.option_e, 'F' : self.option_f,
            'G' : self.option_g, 'H' : self.option_h, 'I' : self.option_i,
            'J' : self.option_j, 'K' : self.option_k, 'L' : self.option_l,
            'M' : self.option_m, 'N' : self.option_n, 'O' : self.option_o,
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
        print('A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M:\n')
        heroes = self.heroes_helper.get_males_heroes()
        App.print_heroes(heroes)
        HeroesHelper.save_heroes_to_csv('males_heroes', heroes)
        request_input()
    

    def option_b(self):
        clear_console()
        print('B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F:\n')
        heroes = self.heroes_helper.get_females_heroes()
        App.print_heroes(heroes)
        HeroesHelper.save_heroes_to_csv('females_heroes', heroes)
        request_input()


    def option_c(self):
        clear_console()
        print('C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M:\n')
        hero = self.heroes_helper.get_more_height_male()
        print(hero)
        HeroesHelper.save_hero_to_csv('more_height_male', hero)
        request_input()

    def option_d(self):
        clear_console()
        print('D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F :\n')
        hero = self.heroes_helper.get_more_height_female()
        print(hero)
        HeroesHelper.save_hero_to_csv('more_height_female', hero)
        request_input()

    def option_e(self):
        clear_console()
        print('E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:\n')
        hero = self.heroes_helper.get_less_height_male()
        print(hero)
        HeroesHelper.save_hero_to_csv('less_height_male', hero)
        request_input()

    def option_f(self):
        clear_console()
        print('F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:\n')
        hero = self.heroes_helper.get_less_height_female()
        print(hero)
        HeroesHelper.save_hero_to_csv('less_height_female', hero)
        request_input()
    
    def option_g(self):
        clear_console()
        print('G - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M:\n')
        average = self.heroes_helper.get_average_height_male()
        print(average)
        HeroesHelper.save_average_height('average_height_male', average)
        request_input()

    def option_h(self):
        clear_console()
        print('H - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F:\n')
        average = self.heroes_helper.get_average_height_female()
        print(average)
        HeroesHelper.save_average_height('average_height_female', average)
        request_input()

    def option_i(self):
        clear_console()
        print('I - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F):\n')
        
        print('C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M:')
        more_height_male = self.heroes_helper.get_more_height_male()
        self.print_hero(more_height_male, False)
        HeroesHelper.save_hero_to_csv('more_height_male_secret', more_height_male, False)
        
        print('\nD - Recorrer la lista y determinar cuál es el superhéroe más alto de género F :')
        more_height_female = self.heroes_helper.get_more_height_female()
        self.print_hero(more_height_male, False)
        HeroesHelper.save_hero_to_csv('more_height_female_secret', more_height_female, False)

        print('\nE - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:')
        less_height_male = self.heroes_helper.get_less_height_male()
        self.print_hero(less_height_male, False)
        HeroesHelper.save_hero_to_csv('less_height_male_secret', less_height_male, False)

        print('\nF - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:')
        less_height_female = self.heroes_helper.get_less_height_female()
        self.print_hero(less_height_female, False)
        HeroesHelper.save_hero_to_csv('less_height_female_secret', less_height_female, False)

        request_input()

    def option_j(self):
        clear_console()
        print('J - Determinar cuántos superhéroes tienen cada tipo de color de ojos:\n')
        quantities = self.heroes_helper.get_grouped_amount_by_eyes_color()
        print(quantities)
        HeroesHelper.save_grouped_amount_by_eyes_color(quantities)
        request_input()

    def option_k(self):
        clear_console()
        print('K - Determinar cuántos superhéroes tienen cada tipo de color de pelo:\n')
        quantities = self.heroes_helper.get_grouped_amount_by_hair_color()
        print(quantities)
        HeroesHelper.save_grouped_amount_by_hair_color(quantities)
        request_input()

    def option_l(self):
        clear_console()
        print('L - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’):\n')
        quantities = self.heroes_helper.get_grouped_amount_by_intelligence()
        print(quantities)
        HeroesHelper.save_grouped_amount_by_intelligence(quantities)
        request_input()

    def option_m(self):
        clear_console()
        print('M - Listar todos los superhéroes agrupados por color de ojos:\n')
        print(self.heroes_helper.get_grouped_by_intelligence())
        request_input()

    def option_n(self):
        clear_console()
        print('N - Listar todos los superhéroes agrupados por color de pelo:\n')
        print(self.heroes_helper.get_grouped_by_intelligence())
        request_input()

    def option_o(self):
        clear_console()
        print('O - Listar todos los superhéroes agrupados por tipo de inteligencia:\n')
        print(self.heroes_helper.get_grouped_by_intelligence())
        request_input()

    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)