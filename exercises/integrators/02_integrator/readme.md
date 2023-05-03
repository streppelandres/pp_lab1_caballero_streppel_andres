Gimnasio - Lista de diccionarios
Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía (por ejemplo, mensual o anual). La información se encuentra almacenada en una lista de listas, donde cada sublista representa a un miembro y contiene los siguientes elementos: número de identificación, nombre, edad y tipo de membresía.


Escriba un programa que permita a los usuarios realizar las siguientes operaciones:


1. Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a la lista de diccionarios.

2. Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).


   3. Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro y el nuevo tipo de membresía. El programa debe buscar el miembro en la lista de diccionario y actualizar el tipo de membresía correspondiente.


   4. Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro. El programa debe buscar el miembro en la lista de diccionarios y mostrar su nombre, edad y tipo de membresía.


   5. Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de diccionarios y calcular el promedio de edad de los miembros.


   6. Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de diccionarios y mostrar el nombre y número de identificación correspondientes.


El programa debe permitir al usuario realizar estas operaciones tantas veces como desee, hasta que decida salir del programa. El programa debe mostrar un menú de opciones para que el usuario pueda elegir la operación que desea realizar.


while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")