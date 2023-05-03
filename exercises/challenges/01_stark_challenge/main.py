import service
import utils

GENDER_MALE = 'M'
GENDER_FEMALE = 'F'

if __name__ == '__main__':
    while True:
        utils.clear_screen()
        print(utils.get_menu())
        match input('Seleccioná una opción:\n').upper():
            case 'A':
                utils.clear_screen()
                print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M:\n')
                print(utils.to_json_dump([{'nombre': hero['nombre'], 'genero': hero['genero']} for hero in service.filter_by_key_value('genero', GENDER_MALE)]))
                utils.request_input()
            case 'B':
                utils.clear_screen()
                print('Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F:\n')
                print(utils.to_json_dump([{'nombre': hero['nombre'], 'genero': hero['genero']} for hero in service.filter_by_key_value('genero', GENDER_FEMALE)]))
                utils.request_input()
            case 'C':
                utils.clear_screen()
                print('Recorrer la lista y determinar cuál es el superhéroe más alto de género M:\n')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_tall_hero_by_gender(GENDER_MALE))))
                utils.request_input()
            case 'D':
                utils.clear_screen()
                print('Recorrer la lista y determinar cuál es el superhéroe más alto de género F:\n')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_tall_hero_by_gender(GENDER_FEMALE))))
                utils.request_input()
            case 'E':
                utils.clear_screen()
                print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:\n')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_lower_hero_by_gender(GENDER_MALE))))
                utils.request_input()
            case 'F':
                utils.clear_screen()
                print('Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:\n')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_lower_hero_by_gender(GENDER_FEMALE))))
                utils.request_input()
            case 'G':
                utils.clear_screen()
                print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género M:\n')
                print(utils.to_json_dump(service.get_sum_by_field_from_list('altura', service.filter_by_key_value('genero', GENDER_MALE))))
                utils.request_input()
            case 'H':
                utils.clear_screen()
                print('Recorrer la lista y determinar la altura promedio de los  superhéroes de género F:\n')
                print(utils.to_json_dump(service.get_sum_by_field_from_list('altura', service.filter_by_key_value('genero', GENDER_FEMALE))))
                utils.request_input()
            case 'I':
                utils.clear_screen()
                print('Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F):\n')
                
                print('C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M:')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_tall_hero_by_gender(GENDER_MALE), False)))

                print('D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F:')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_tall_hero_by_gender(GENDER_FEMALE), False)))

                print('E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M:')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_lower_hero_by_gender(GENDER_MALE), False)))

                print('F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F:')
                print(utils.to_json_dump(service.get_hero_info(service.get_most_lower_hero_by_gender(GENDER_FEMALE), False)))

                utils.request_input()
            case 'J':
                utils.clear_screen()
                print('Determinar cuántos superhéroes tienen cada tipo de color de ojos.:\n')
                print(utils.to_json_dump(service.group_by_key_get_amount('color_ojos')))
                utils.request_input()
            case 'K':
                utils.clear_screen()
                print('Determinar cuántos superhéroes tienen cada tipo de color de pelo:\n')
                print(utils.to_json_dump(service.group_by_key_get_amount('color_pelo')))
                utils.request_input()
            case 'L':
                utils.clear_screen()
                print('Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’):\n')
                print(utils.to_json_dump(service.group_by_key_get_amount('inteligencia')))
                utils.request_input()
            case 'M':
                utils.clear_screen()
                print('Listar todos los superhéroes agrupados por color de ojos.:\n')
                print(utils.to_json_dump(service.group_by_key('color_ojos')))
                utils.request_input()
            case 'N':
                utils.clear_screen()
                print('Listar todos los superhéroes agrupados por color de pelo.:\n')
                print(utils.to_json_dump(service.group_by_key('color_pelo')))
                utils.request_input()
            case 'O':
                utils.clear_screen()
                print('Listar todos los superhéroes agrupados por tipo de inteligencia:\n')
                print(utils.to_json_dump(service.group_by_key('inteligencia')))
                utils.request_input()
            case 'X':
                utils.clear_screen()
                print('Adiós :(')
                exit(0)
            case _:
                print('Opción incorrecta, vuelva a intentar\n')