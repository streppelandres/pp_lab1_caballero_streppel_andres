import copy
import data as data

API_RESPONSE = data.lista_personajes

def get_all_names():
    return list(map(lambda heroe : heroe['nombre'], API_RESPONSE))

def get_all_names_heights():
    return list(map(lambda heroe : heroe['nombre'] + ' - ' + str(round(float(heroe['altura']) / 100, 2)), API_RESPONSE))

def get_most_big_generic_by_field(field, hide_identity):
    hero = None
    for i in range(0, len(API_RESPONSE)):
        if hero == None or float(hero[field]) < float(API_RESPONSE[i][field]):
            hero = copy.copy(API_RESPONSE[i]) # No sabia que Python te guarda una referencia acá y ya me arruga la ropa modificar la logica
    if hide_identity:
        # Y como esta guardando una referencia me modifica esto en el listado original
        hero['identidad'] = '*******'
    return hero

def get_most_small_generic_by_field(field, hide_identity):
    hero = None
    for i in range(0, len(API_RESPONSE)):
        if hero == None or float(hero[field]) > float(API_RESPONSE[i][field]):
            hero = copy.copy(API_RESPONSE[i]) # No sabia que Python te guarda una referencia acá y ya me arruga la ropa modificar la logica
    if hide_identity:
        # Y como esta guardando una referencia me modifica esto en el listado original
        hero['identidad'] = '*******'
    return hero

def get_average_generic_by_field(field):
    average = 0
    for heroe in API_RESPONSE:
        average += float(heroe[field])
    return round((average / len(API_RESPONSE)) / 100, 2)