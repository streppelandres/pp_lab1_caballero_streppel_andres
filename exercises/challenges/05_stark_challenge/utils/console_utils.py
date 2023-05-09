import os
import json

def print_json(element):
    print(json.dumps(element, indent=4))

def clear_console():
    os.system('clear')

def request_input():
    input('\nPresione una tecla para continuar...\n')