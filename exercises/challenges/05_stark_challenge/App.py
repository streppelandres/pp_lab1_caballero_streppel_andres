from utils.json_utils import load_json
from utils.config_utils import load_config
from utils.console_utils import *

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/config.ini'

class App:
    heroes: list
    menu: str
    options : dict
    
    def __init__(self):
        '''
        Initialize the app, load the heroes data, ini config file and menu options
        '''
        self.heroes = load_json(JSON_DATA_PATH)
        self.config = load_config(INI_CONFIG_PATH)
        self.options = {
            'A' : self.option_a,
            'B' : self.option_b,
            'X' : self.option_exit
        }


    def start(self):
        while True:
            clear_console()
            option = input(self.config['TEXT']['menu'] + '\n').upper()
            if option in self.options:
                self.options[option]()
            else:
                print('Opción incorrecta, vuelva a intentar\n')


    def option_a(self):
        clear_console()
        print_json(self.heroes)
        request_input()
    

    def option_b(self):
        clear_console()
        print('Hi! I am the option B')
        request_input()


    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)