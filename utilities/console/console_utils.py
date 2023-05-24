import os
import json

def print_json(element:any) -> None:
    '''
    Prints to the console in JSON format
    '''
    print(json.dumps(element, indent=4))

def clear_console() -> None:
    '''
    Clear console
    '''
    os.system('clear')

def request_input(message:str='Presione una tecla para continuar...') -> None:
    '''
    Ask the user to enter something, do nothing with that value
        message: Display text
    '''
    input(f'\n{message}\n')

# TODO: Pasarlo a regex si no el profe se enoja
def request_int(message:str, retry_message:str='Please, try again') -> int:
    '''
    Recursively requests an integer until it is a valid numeric
        message: Display text
        retry_message: Optional retry message to display
        returns: Valid user input
    '''
    n = input(f'\n{message}\n')
    if n.isnumeric():
        return int(n)
    print(f'\n{retry_message}\n')
    request_int(message, retry_message)

# TODO: Pasarlo a regex si no el profe se enoja
def request_int_in_range(message:str, range_start:int, range_end:int, retry_message:str='Please, try again') -> int:
    n = input(f'\n{message}\n')
    if n.isnumeric() and n >= range_start and n <= range_end:
        return int(n)
    print(f'\n{retry_message}\n')
    request_int(message, retry_message)

# TODO: Hacer otro que sea con Regex
def request_string(message:str, valid_words:list, retry_message:str='Please, try again') -> bool:
    '''
    Recursively requests an string until it is a valid word
        message: Display text
        valid_words: Valid words array to match
        retry_message: Optional retry message to display
        returns: Valid user input
    '''
    word = input(message).lower()
    if word in [w.lower() for w in valid_words]:
        return word
    print(retry_message)
    request_string(message, valid_words, retry_message)

def print_elements_in_str(elements:list) -> None:
    '''
    Prints to the console each element of the list in __str__()
        elements: Elements to print
    '''
    [print(e.__str__()) for e in elements]