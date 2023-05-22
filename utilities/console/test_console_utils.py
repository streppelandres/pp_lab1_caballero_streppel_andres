import console_utils

#FIXME: these are not real test's, idk yet how to test the console or if is possible to do

__DICTIONARY = [{'key': 'value', 'key2': 'value'}, {'key': 'value', 'key2': 'value'}]

def test_print_json():
    console_utils.print_json(__DICTIONARY)

test_print_json()

def test_clear_console():
    print('This is gonna be cleared')
    console_utils.clear_console()
    print('But this is going to be visible 😎')

test_clear_console()

def test_request_input():
    console_utils.request_input()

test_request_input()

def test_request_int():
    integer = console_utils.request_int('Please, enter a number: ', 'Valid numbers, please, try again')
    print(f'Entered number: {integer}')

test_request_int()

def test_request_string():
    valid_words = ['Uva', 'Mora', 'Pomelo']
    word = console_utils.request_string(f'Select a option {valid_words}:', valid_words, f'Please enter one of these: {valid_words}')
    print(f'Selected option: {word}')

test_request_string()

def test_print_elements_in_str():
    console_utils.print_elements_in_str(__DICTIONARY)

test_print_elements_in_str()