import os
import json

def json_dump(element):
    return json.dumps(element, indent=4)

def print_json(element):
    print(json_dump(element))

def clear_screen():
    os.system('clear')

def request_input():
    input('\nPresione una tecla para continuar...\n')