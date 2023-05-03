import utils

def normalize_data(heroes):
    if not heroes:
        print('Error: Lista de héroes vacía')
        return
    
    def normalize_hero(hero):
        return {
            'name': hero['nombre'],
            'identity': hero['identidad'],
            'company': hero['empresa'],
            'height': float(hero['altura']),
            'weight': float(hero['peso']),
            'genre': hero['genero'] == 'M' and 'Male' or 'Female',
            'eyes_color': hero['color_ojos'],
            'hair_color': hero['color_pelo'],
            'strength': int(hero['fuerza']),
            'intelligence': hero['inteligencia']
        }
    
    return list(map(normalize_hero, heroes))


def get_hero_name(hero):
    return f'Name: {hero["name"]}'


def print_data(element):
    print(element)


def print_heroes_names(heroes):
    if not heroes:
        print('Error: Lista de héroes vacía')
        return
    
    for hero in heroes:
        print_data(get_hero_name(hero))


def print_heroe_name_and_attr(hero, atrr_key):
    print(f'{get_hero_name(hero)} | {atrr_key}: {hero[atrr_key]}')


def print_heroes_names_and_heights(heroes):
    if not heroes:
        print('Error: Lista de héroes vacía')
        return
    
    for hero in heroes:
        print_heroe_name_and_attr(hero, 'height')

def filter_hero_by_attr_key_and_value(heroes, attr_key, attr_value):
    return filter(lambda hero: hero[attr_key] == attr_value, heroes)


def get_max_hero_by_attr(heroes, attr_key):
    return max(heroes, key=lambda hero : float(hero[attr_key]))


def get_min_hero_by_attr(heroes, attr_key):
    return min(heroes, key=lambda hero : float(hero[attr_key]))


def get_max_or_min_hero_by_attr(heroes, calc_max:bool, attr_key:str):
    return calc_max and get_max_hero_by_attr(heroes, attr_key) or get_min_hero_by_attr(heroes, attr_key)


def get_max_or_min_hero_by_attr(heroes, calc_max:bool, attr_key:str):
    print(f'{calc_max and "Max" or "Min"} {atrr_key}: {print_heroe_name_and_attr(get_max_or_min_hero_by_attr(heroes, calc_max, atrr_key), atrr_key)}')


def get_sum_by_hero_attr(heroes, attr_key):
    return sum([hero[attr_key] for hero in heroes])


def get_avergae_by_hero_attr(heroes, attr_key):
    return get_sum_by_hero_attr(heroes, attr_key) / len(heroes)


def get_heroes_height_average(heroes):
    return get_avergae_by_hero_attr(heroes, 'height')


def group_heroes_by_key(heroes, key):
    grouped_heroes = {}
    for hero in heroes:
        if key == 'intelligence' and not hero['intelligence'] : # no esta bueno porque estaría manipulando la data
            hero['intelligence'] = 'No tiene' # y tipo, podría ser más generico

        if hero[key] in grouped_heroes.keys():
            grouped_heroes[hero[key]].append(hero)
        else:
            grouped_heroes[hero[key]] = []
            grouped_heroes[hero[key]].append(hero)
    return grouped_heroes

def group_heroes_by_key_get_amount(heroes, key):
    grouped_heroes = group_heroes_by_key(heroes, key)
    return {k: len(grouped_heroes[k]) for k in grouped_heroes}

def get_menu():
    return "".join(['A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n',
    'B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n',
    'C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n',
    'D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n',
    'E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M \n',
    'F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F \n',
    'G - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M\n',
    'H - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F\n',
    'I - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n',
    'J - Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n',
    'K - Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n',
    'L - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).\n', 
    'M - Listar todos los superhéroes agrupados por color de ojos.\n',
    'N - Listar todos los superhéroes agrupados por color de pelo.\n',
    'O - Listar todos los superhéroes agrupados por tipo de inteligencia\n',
    'X - Salir'])

def main_menu():
    print(get_menu())
    return input('Seleccioná una opción:\n').upper()

def app(heroes):
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    heroes = normalize_data(heroes)
    match main_menu():
        case 'A':
            utils.clear_screen()
            print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M:\n')
            print_heroes_names(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_MALE)))
            utils.request_input()
        case 'B':
            utils.clear_screen()
            print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F:\n')
            print_heroes_names(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_FEMALE)))
            utils.request_input()
        case 'C':
            utils.clear_screen()
            print('Recorrer la lista y determinar cuál es el superhéroe más alto de género M:\n')
            print_data(get_max_hero_by_attr(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_MALE)), 'height'))
            utils.request_input()
        case 'D':
            utils.clear_screen()
            print('Recorrer la lista y determinar cuál es el superhéroe más alto de género F:\n')
            print_data(get_max_hero_by_attr(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_FEMALE)), 'height'))
            utils.request_input()
        case 'E':
            utils.clear_screen()
            print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:\n')
            print_data(get_min_hero_by_attr(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_MALE)), 'height'))
            utils.request_input()
        case 'F':
            utils.clear_screen()
            print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:\n')
            print_data(get_min_hero_by_attr(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_FEMALE)), 'height'))
            utils.request_input()
        case 'G':
            utils.clear_screen()
            print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género M:\n')
            print_data(get_heroes_height_average(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_MALE))))
            utils.request_input()
        case 'H':
            utils.clear_screen()
            print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género F:\n')
            print_data(get_heroes_height_average(list(filter_hero_by_attr_key_and_value(heroes, 'genre', GENDER_FEMALE))))
            utils.request_input()
        case 'I':
            utils.clear_screen()
            print('Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F):\n')
            
            print('C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M:')

            print('D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F:')

            print('E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:')

            print('F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:')

            utils.request_input()
        case 'J':
            utils.clear_screen()
            print('Determinar cuántos superhéroes tienen cada tipo de color de ojos.:\n')
            print_data(utils.json_dump(group_heroes_by_key_get_amount(heroes, 'eyes_color')))
            utils.request_input()
        case 'K':
            utils.clear_screen()
            print('Determinar cuántos superhéroes tienen cada tipo de color de pelo:\n')
            print_data(utils.json_dump(group_heroes_by_key_get_amount(heroes, 'hair_color')))
            utils.request_input()
        case 'L':
            utils.clear_screen()
            print('Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’):\n')
            print_data(utils.json_dump(group_heroes_by_key_get_amount(heroes, 'intelligence')))
            utils.request_input()
        case 'M':
            utils.clear_screen()
            print('Listar todos los superhéroes agrupados por color de ojos.:\n')
            print_data(utils.json_dump(group_heroes_by_key(heroes, 'eyes_color')))
            utils.request_input()
        case 'N':
            utils.clear_screen()
            print('Listar todos los superhéroes agrupados por color de pelo.:\n')
            print_data(utils.json_dump(group_heroes_by_key(heroes, 'hair_color')))
            utils.request_input()
        case 'O':
            utils.clear_screen()
            print('Listar todos los superhéroes agrupados por tipo de inteligencia:\n')
            print_data(utils.json_dump(group_heroes_by_key(heroes, 'intelligence')))
            utils.request_input()
        case 'X':
            utils.clear_screen()
            print('Adiós :(')
            exit(0)
        case _:
            print('Opción incorrecta, vuelva a intentar\n')
