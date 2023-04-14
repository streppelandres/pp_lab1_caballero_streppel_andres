import os

def get_menu():
    return "".join([
    '1- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe\n',
    '2- Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo\n',
    '3- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)\n',
    '4- Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)\n',
    '5- Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)\n',
    '6- Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)\n',
    '7- Calcular e informar cual es el superhéroe más y menos pesado.\n',
    '8- Salir'])

def clear_screen():
    os.system('clear')

def request_input():
    input('\nPresione una tecla para continuar...\n')