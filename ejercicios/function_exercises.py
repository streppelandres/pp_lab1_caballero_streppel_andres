import math

'''
Crear una función que convierta grados Celsius a grados Fahrenheit.
Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
'''
def celsius_to_fahrenheit(celcius_degrees):
    return celcius_degrees * 1.8 + 32

#print(celsius_to_fahrenheit(32))

'''
Crear una función que calcule el área de un círculo.
Recibe un parámetro (radio) y devuelve el área del círculo.
'''
def calc_circle_area(radius):
    return math.pi * pow(radius, 2)

#print(calc_circle_area(25))

'''
Crear una función que calcule el descuento aplicado a un producto.
Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
'''
def calc_product_disconted_porcent(price, disconted_price):
    return ((price - disconted_price) / price) * 100

#print(calc_product_disconted_porcent(100, 20))

'''
Crear una función que calcule el promedio de edad de un grupo de personas.
Recibe una lista de edades y devuelve el promedio.
'''
def calc_average_from_ages(ages_list):
    return sum(ages_list) / len(ages_list)

#print(calc_average_from_ages([81, 2, 34, 21, 4, 1]))

'''
Crear una función que determine si un número es primo o no.
Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
'''
def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5)+1))

#print(is_prime(3))

'''
Crear una función que calcule el área de un triángulo.
Recibe dos parámetros (base y altura) y devuelve el área.
'''
def calc_triangle_area(base, height):
    return (base * height) / 2

#print(calc_triangle_area(2, 4))

'''
Crear una función que calcule el máximo común divisor de dos números.
Recibe dos parámetros (números) y devuelve el máximo común divisor.
'''
def calc_max_common_divisor(number_a, number_b):
    return math.gcd(number_a, number_b) # soy programador, no me gusta pensar

#print(calc_max_common_divisor(4, 3))

'''
Crear una función que verifique si un número es par o impar.
Recibe un número como parámetro y devuelve True si es par o False si es impar.
'''
def is_pair(number):
    return number % 2 == 0

#print(is_pair(3))

'''
Crear una función que cuente la cantidad de veces que aparece un elemento en una lista.
Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
'''
def count_element_in_list(element, elements):
    return len(list(filter(lambda e : e == element, elements)))

#print(count_element_in_list('Hola', ['Chau', 'Chau', 'Hola', 'Chau', 'Hola']))

'''
Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
'''
def get_large_word_from_list(words):
    return max(words, key=len) # me lo enseñó chatgpt

#print(get_large_word_from_list(['Gato', 'Perro', 'Cobayo', 'Rinoceronte', 'Canario']))

'''
Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
'''
def count_vocals(word):
    return sum([1 for char in range(len(word)) if word[char] in ['a', 'e', 'i', 'o', 'u']])

#print(count_vocals('Hola mundo!'))

'''
Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
'''
def get_repeated_names(names_a, names_b):
    repeated_names = []
    for name in names_a:
        if name in names_b:
            repeated_names.append(name)
    return repeated_names

#print(get_repeated_names(['Pomelo', 'Mora', 'Uva'], ['Yeni', 'Mora', 'Yesi', 'Pomelo', 'Mili']))

'''
Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
'''
def list_to_dic_with_len(words):
    words_with_len = {}
    for word in words:
        words_with_len[word] = len(word)
    return words_with_len

#print(list_to_dic_with_len(['Pomelo', 'Mora', 'Uva', 'Negra', 'Milka']))

'''
Crear una función que recibe una lista de números y devuelve un diccionario
con el valor mínimo, el valor máximo y el promedio de los números en la lista.
'''
def list_to_dic_with_min_max_average(numbers):
    return {
        'minimum': min(numbers),
        'maximum': max(numbers),
        'average': sum(numbers) / len(numbers)
    }

#print(list_to_dic_with_min_max_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

'''
Crear una función que recibe una lista de diccionarios con información de películas (título, género, director)
y devuelve un diccionario con la cantidad de películas por género.
'''
def movies_dic_to_genre_count(movies):
    genre_movie_count = {}
    for movie in movies:
        if movie['genre'] in genre_movie_count.keys():
            genre_movie_count[movie['genre']] += 1
        else:
            genre_movie_count[movie['genre']] = 1
    return genre_movie_count

#print(movies_dic_to_genre_count([
#    {'title':'The Mommy', 'genre': 'fantasy', 'director': 'Fulano'},
#    {'title':'Titanic', 'genre': 'romantic', 'director': 'Cameron'},
#    {'title':'Harry Potter', 'genre': 'fantasy', 'director': 'Mengano'},
#    {'title':'Batman Dark Night', 'genre': 'accion', 'director': 'Nolan'},
#    {'title':'Saw', 'genre': 'horror', 'director': 'Cosme'}
#]))