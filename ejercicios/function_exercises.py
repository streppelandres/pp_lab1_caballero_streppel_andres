import math

'''
Crear una función que convierta grados Celsius a grados Fahrenheit.
Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
'''
def celsius_to_fahrenheit(celcius_degrees):
    return celcius_degrees * 1.8 + 32

'''
Crear una función que calcule el área de un círculo.
Recibe un parámetro (radio) y devuelve el área del círculo.
'''
def calc_circle_area(radius):
    return pow(math.pi * radius, 2)

'''
Crear una función que calcule el descuento aplicado a un producto.
Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
'''
def calc_product_disconted_porcent(price, disconted_price):
    return (price * disconted_price) / 100

'''
Crear una función que calcule el promedio de edad de un grupo de personas.
Recibe una lista de edades y devuelve el promedio.
'''
def calc_average_from_ages(ages_list):
    return sum(ages_list) / len(ages_list)

'''
Crear una función que determine si un número es primo o no.
Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
'''
def is_prime(number):
    return list(filter(lambda x: (number > 2 and number % x != 0), range(2, int(number**0.5) + 1)))

'''
Crear una función que calcule el área de un triángulo.
Recibe dos parámetros (base y altura) y devuelve el área.
'''
def calc_triangle_area(base, height):
    return (base * height) / 2

'''
Crear una función que calcule el máximo común divisor de dos números.
Recibe dos parámetros (números) y devuelve el máximo común divisor.
'''
def calc_max_common_divisor(number_a, number_b):
    return math.gcd(number_a, number_b) # soy programador, no me gusta pensar

'''
Crear una función que verifique si un número es par o impar.
Recibe un número como parámetro y devuelve True si es par o False si es impar.
'''
def is_pair(number):
    return number % 2 == 0

'''
Crear una función que cuente la cantidad de veces que aparece un elemento en una lista.
Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
'''
def count_element_in_list(element, elements):
    return len(list(filter(lambda e : e == element, elements)))

'''
Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
'''
def get_large_word_from_list(words):
    largest_word = None
    return list(filter(lambda w : largest_word == None or len(w) > largest_word, words))

'''
Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
'''
def count_vocals(word):
    return sum([1 for char in range(len(word)) if word[char] in ['a', 'e', 'i', 'o', 'u']])

'''
Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
'''
def get_repeated_names(names_a, names_b):
    repeated_names = []
    for name in names_a:
        if name in names_b:
            repeated_names.append(name)
    return repeated_names

'''
Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
'''
def list_to_dic_with_len(words):
    words_with_len = {}
    for word in words:
        words_with_len[word] = len(word)
    return words_with_len

'''
Crear una función que recibe una lista de números y devuelve un diccionario
con el valor mínimo, el valor máximo y el promedio de los números en la lista.
'''
def list_to_dic_with_min_max_prom(numbers):
    return {
        'minimum': min(numbers),
        'maximum': max(numbers),
        'average': sum(numbers) / len(numbers)
    }

'''
Crear una función que recibe una lista de diccionarios con información de películas (título, género, director)
y devuelve un diccionario con la cantidad de películas por género.
'''
def movies_dic_to_genre_count(movies):
    genre_movie_count = {}
    for movie in movies:
        genre_movie_count[movie['genre']] += 1
    return genre_movie_count