import os
import json

def print_json(element):
    print(json.dumps(element, indent=4))

def clear_console():
    os.system('clear')

def request_input():
    input('\nPresione una tecla para continuar...\n')

def request_int(message:str) -> int:
    n = input(f'\n{message}')
    if not n.isnumeric():
        request_int(message)
    return int(n)

# TODO: Pasar las validaciones a RegEx, si no se enojan los profes
def request_string(message:str, valid_words:list) -> bool:
    word = input(message).lower()
    if word in valid_words:
        return word
    request_string(message, valid_words)

def print_elements_in_str(elements:list):
    [print(e.__str__()) for e in elements]