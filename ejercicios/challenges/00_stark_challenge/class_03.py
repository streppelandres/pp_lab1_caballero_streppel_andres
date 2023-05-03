import class_03_repository as repo
import class_03_utils as utils

if __name__ == '__main__':
    while True:
        utils.clear_screen()
        print(utils.get_menu())
        match int(input('Seleccioná una opción:\n')):
            case 1:
                utils.clear_screen()
                print('Mostrando nombres de los superhéroes:\n')
                print(repo.get_all_names())
                utils.request_input()
            case 2:
                utils.clear_screen()
                print('Mostrando nombres y altura de los superhéroes:\n')
                print(repo.get_all_names_heights())
                utils.request_input()
            case 3:
                utils.clear_screen()
                print('Mostrando el personaje más alto:\n')
                print(repo.get_most_big_generic_by_field('altura', True))
                utils.request_input()
            case 4:
                utils.clear_screen()
                print('Mostrando el personaje más bajo:\n')
                print(repo.get_most_small_generic_by_field('altura', True))
                utils.request_input()
            case 5:
                utils.clear_screen()
                print('Mostrando el promedio de altura:\n')
                print(repo.get_average_generic_by_field('altura'))
                utils.request_input()
            case 6:
                utils.clear_screen()
                print('Mostrando el personaje más alto con su identidad:\n')
                print(repo.get_most_big_generic_by_field('altura', False))
                print('\nMostrando el personaje más bajo con su identidad:\n')
                print(repo.get_most_small_generic_by_field('altura', False))
                utils.request_input()
            case 7:
                utils.clear_screen()
                print('Mostrando el personaje más pesado con su identidad:\n')
                print(repo.get_most_big_generic_by_field('peso', False))
                print('\nMostrando el personaje más liviano con su identidad:\n')
                print(repo.get_most_small_generic_by_field('peso', False))
                utils.request_input()
            case 8:
                utils.clear_screen()
                print('Adiós :(')
                exit(0)
            case _:
                print('Opción incorrecta, vuelva a intentar\n')