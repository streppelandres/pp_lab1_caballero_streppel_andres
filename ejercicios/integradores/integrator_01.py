import os

members_id, members_name, members_age, members_membership = [31, 8, 2], ['Mora', 'Pomelo', 'Uva'], [12, 5, 1], ['ANUAL', 'MENSUAL', 'MENSUAL']

def print_menu():
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")

def clean_console():
    os.system('clear')

def print_member_by_index(i):
    print(f'Member id [{members_id[i]}], name [{members_name[i]}], age [{members_age[i]}], membership [{members_membership[i]}]')

def get_member_index_by_id(id):
    return members_id.index(id)

def add_member():
    print('Agregando un nuevo miembro:\n')
    members_id.append(int(input('Ingrese un ID:\n')))
    members_name.append(input('Ingrese un nombre:\n'))
    members_age.append(int(input('Ingrese la edad:\n')))
    members_membership.append(input('Ingrese la membresía [ANUAL/MENSUAL]\n').upper())

def show_all_members():
    clean_console()
    print('Mostrando informacion:\n')
    for i in range(0, len(members_id)):
        print_member_by_index(i)
    print('\n')

def update_member_membership():
    clean_console()
    index = get_member_index_by_id(int(input('Ingrese id del miembro a actualizar su membresía\n')))
    members_membership[index] = members_membership[index] == 'ANUAL' and 'MENSUAL' or 'ANUAL'
    print('Membresía actualizada\n')
    print_member_by_index(index)

def find_member():
    clean_console()
    print_member_by_index(get_member_index_by_id(int(input('Ingrese id del miembro a buscar:\n'))))

def calculate_average():
    clean_console()
    print(f'El promedio de edad es [{sum(members_age) / len(members_age)}]')

def find_old_and_young_member():
    clean_console()
    oldest_member_age, young_member_age = 0, 0
    oldest_member_index, young_member_index = None, None
    for i in range(0, len(members_id)):
        if members_age[i] > oldest_member_age:
            oldest_member_age = members_age[i]
            oldest_member_index = i
        if young_member_index == None or members_age[i] < young_member_age:
            young_member_age = members_age[i]
            young_member_index = i
    print(f'El miembro más viejo es:')
    print_member_by_index(oldest_member_index)
    print(f'El miembro más joven es:')
    print_member_by_index(young_member_index)

if __name__ == "__main__":
    while True:
        print_menu()
        match int(input('\nIngrese una opción:\n')):
            case 1:
                add_member()
            case 2:
                show_all_members()
            case 3:
                update_member_membership()
            case 4:
                find_member()
            case 5:
                calculate_average()
            case 6:
                find_old_and_young_member()
            case 0:
                exit(0)
            case _:
                print('\nOpción incorrecta, pruebe nuevamente')
