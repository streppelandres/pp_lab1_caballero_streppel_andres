'''
Crea una lista con los números del 1 al 10 e imprime solo los números impares.
'''
def ejercicio_1():
    print(list(filter(lambda n : n % 2 == 0, range(1, 10))))
#ejercicio_1()

'''
Crea una lista con 5 números enteros.
Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado.
Finalmente imprime todos los números
'''
def ejercicio_2():
    print([1, 2, int(input('Ingrese un número\n')), 4, 5])
#ejercicio_2()

'''
Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo.
Luego, muestra la suma de todos los números ingresados.
'''
def ejercicio_3():
    # print(sum([int(input("Ingrese un número: ")) for _ in iter(int, -1)]))
    numbers = []
    while True:
        number = int(input('Ingrese un número:\n'))
        if number < 0:
            break        
        numbers.append(number)
    print(sum(numbers))
#ejercicio_3()

'''
Crea una lista vacía y pide al usuario que ingrese una palabra.
Luego, muestra la primera letra de la palabra.
Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".
'''
def ejercicio_4():
    # ¿Y para que quiero la lista vacía?
    while True:
        word = input('Ingrese una palabra:\n')
        print(word[0])
        if word[0].lower() == 'z':
            break
#ejercicio_4()

'''
Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.
'''
def ejercicio_5():
    print(['Avellaneda', 'Lomas de Zamora', 'Banfield', 'Temperley', 'Lanús'][-1])
#ejercicio_5()

'''
Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.
'''
def ejercicio_6():
    l = [1, 2, 3]
    l.append(4)
    print(l)
#ejercicio_6()

'''
Crea una lista con los nombres de tus 3 deportes favoritos y luego agrega otro deporte al final de la lista.
'''
def ejercicio_7():
    l = ['Da pedotita', 'Da pedotita', 'Da pedotita']
    l.append('Da pedotita')
    print(l)
#ejercicio_7()

'''
Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.
'''
def ejercicio_8():
    print(['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'][0:3])
#ejercicio_8()

'''
Crea una lista de números enteros y pide al usuario que ingrese otro número entero.
Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra.
Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró
'''
def ejercicio_9():
    i = [3, 2, 8, 4, 7, 1, 9].index(int(input('Ingrese un número a buscar:\n')))
    print(i and f'Se encontró el número en la posición {i}' or 'No se encontró el número')
#ejercicio_9()

'''
Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.
'''
def ejercicio_10():
    print(list(filter(lambda word : len(word) > 5, ['gato', 'perro', 'cobayo', 'conejo', 'cotorrita'])))
#ejercicio_10()

'''
Crea una lista de palabras y pide al usuario que ingrese una palabra.
Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.
'''
def ejercicio_11():
    word = input('Ingrese una palabra:\n')
    print(list(filter(lambda w : len(w) == len(word), ['gato', 'perro', 'cobayo', 'conejo', 'cotorrita'])))
#ejercicio_11()

'''
Crea una lista con los nombres de tus 3 películas favoritas
y luego imprime los elementos en orden inverso (sin utilizar el método reverse())
'''
def ejercicio_12():
    movies = ['Movie 1', 'Movie 2', 'Movie 3']
    i = len(movies) - 1
    while i >= 0:
        print(movies[i])
        i-=1
ejercicio_12()

'''
Crea una lista de números y encuentra el promedio de todos los números en la lista.
'''

'''
Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.
'''

'''
Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.
'''

'''
Crea dos listas con la misma cantidad de elementos
y luego crea una tercera lista que contenga los elementos de ambas listas intercalados.
Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].
'''

'''
Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.
'''

'''
Solicitar al usuario números enteros hasta que ingrese el 0.
Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())
'''

'''
Crea una lista vacía y pide al usuario que ingrese una palabra.
Luego, agrega la palabra a la lista si no se encuentra ya en la lista.
Repite este proceso hasta que la lista tenga al menos 5 palabras.
'''

'''
A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el promedio y la suma total de todos los elementos
'''

'''
Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos.
Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.
'''

'''
Crear un programa que solicite al usuario ingresar: nombre del producto, cantidad y precio unitario.
Guardar los datos en 3 listas distintas. Solicitar productos hasta que el nombre del producto sea ‘xxx’.
Luego imprimir la lista de artículos con el siguiente formato:
nombre_articulo	cantidad	$ precio_unitario 	$ total
	Ejemplo:
	alfajor capitan del espacio		6	$ 150		$ 900
'''