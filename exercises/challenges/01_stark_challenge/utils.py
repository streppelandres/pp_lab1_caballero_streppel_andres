import os
import json

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

def clear_screen():
    os.system('clear')

def request_input():
    input('\nPresione una tecla para continuar...\n')

def to_json_dump(element):
    return json.dumps(element, indent=4)