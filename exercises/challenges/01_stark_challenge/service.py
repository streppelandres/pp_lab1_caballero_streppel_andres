import data

def filter_by_key_value(key, value):
    return filter(lambda hero: hero[key] == value, data.heroes)


def group_by_key(key):
    grouped_heroes = {}
    for hero in data.heroes:
        if key == 'inteligencia' and not hero['inteligencia'] : # no esta bueno porque estaría manipulando la data
            hero['inteligencia'] = 'No tiene' # y tipo, podría ser más generico

        if hero[key] in grouped_heroes.keys():
            grouped_heroes[hero[key]].append(hero)
        else:
            grouped_heroes[hero[key]] = []
            grouped_heroes[hero[key]].append(hero)
    return grouped_heroes


def group_by_key_get_amount(key):
    grouped_heroes = group_by_key(key)
    return {k: len(grouped_heroes[k]) for k in grouped_heroes}


def get_max_by_field_from_list(field, elements):
    return max(elements, key=lambda hero : float(hero[field]))


def get_min_by_field_from_list(field, elements):
    return min(elements, key=lambda hero : float(hero[field]))


def get_sum_by_field_from_list(field, elements):
    return sum([float(hero[field]) for hero in elements if '.' in hero[field]])


def get_hero_info(hero, hide_identity=True):
    return {'nombre': hero['nombre'], 'genero': hero['genero'], 'altura': hero['altura'], 'identidad': hide_identity and 'secreta' or hero['identidad']}


def get_most_lower_hero_by_gender(gender):
    return get_min_by_field_from_list('altura', filter_by_key_value('genero', gender))


def get_most_tall_hero_by_gender(gender):
    return get_max_by_field_from_list('altura', filter_by_key_value('genero', gender))