from utils.json_utils import load_json
from utils.config_utils import load_config

JSON_DATA_PATH = './data/heroes.json'
INI_CONFIG_PATH = './config/config.ini'

class App:
    heroes: list
    menu: str
    
    def __init__(self):
        self.heroes = load_json(JSON_DATA_PATH)
        self.menu = load_config(INI_CONFIG_PATH)['TEXT']['menu']


    def get_menu(self):
        return self.menu


    def option_a(self):
        print('Hi! I am the option A')
        print(self.heroes)
        input('Esperando que ingreses una opción')
    

    def option_b(self):
        print('Hi! I am the option B')


    def option_exit(self):
        print('Cyaaa 👋')
        exit(0)