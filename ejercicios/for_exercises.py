from math import sqrt

hardcoded_numbers = [10, -50, 73, 0, 88, -20, -16, 55, 42, -81, 94, 39, -3, -69, -11, -84, 64, -48, -18, -98, -27,
         -91, 12, 28, 49, -29, -32, 51, -94, 80, 35, 26, -57, -39, -63, -87, -90, -53, -9, 7, 66, -43, -85, 20, 19,
          86, -65, 17, 44, 61, -76]
hardcoded_words = ['manzana', 'guitarra', 'perro', 'casa', 'gato', 'coche', 'libro', 'fútbol', 'montaña', 'playa',
       'bici', 'jardín', 'galleta', 'chocolate', 'café', 'película', 'televisor', 'sol', 'lluvia', 'nieve',
       'mesa', 'silla', 'computadora', 'ojo', 'ratón', 'teclado', 'planta', 'pintura', 'teléfono', 'reloj',
       'hamburguesa', 'anana', 'ensalada', 'pollo', 'pescado', 'arroz', 'frijoles', 'sopa', 'postre', 'leche',
       'vino', 'cerveza', 'agua', 'fuego', 'aire', 'tierra', 'mar', 'río', 'cielo', 'estrella']

'''
Dada una lista de números, imprimir el número más grande de la lista.
'''
def ejercicio_1():
    r = 0
    for n in hardcoded_numbers:
       r = n > r and n or r
    print(f'El número más grande es: {r}')
#ejercicio_1()

'''
Dada una lista de palabras, imprimir la palabra más larga de la lista.
'''
def ejercicio_2():
    large_word = ''
    for word in hardcoded_words:
        large_word = len(large_word) < len(word) and word or large_word
    print(f'La palabra más larga es: {large_word}')

#ejercicio_2()

'''
Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n
'''
def ejercicio_3():
    number = int(input('Ingresar un número:\n'))
    for n in range(1, number + 1):
        if(n % 2 == 0):
            print(n)

#ejercicio_3()

'''
Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.
'''
def ejercicio_4():
    number = int(input('Ingresar un número:\n'))
    amount = 0
    for n in range(1, number + 1):
        if(n % 2 != 0):
            amount = amount + n
    print(amount)
#ejercicio_4()

'''
Dada una lista de números, imprimir el número más pequeño de la lista.
'''
def ejercicio_5():
    most_litte_number = None
    for n in hardcoded_numbers:
        if(not most_litte_number or most_litte_number > n):
            most_litte_number = n
    print(most_litte_number)
#ejercicio_5()

'''
Dada una lista de palabras, imprimir la cantidad total de vocales en la lista
'''
def ejercicio_6():
    vocals = 0
    for w in hardcoded_words:
        for l in range(0, len(w)):
            if(w[l] in ['a', 'e', 'i', 'o', 'u']):
                vocals = vocals + 1
    print(vocals)
#ejercicio_6()

'''
Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n
'''
def ejercicio_7():
    # Igual que el 3
    ejercicio_3()
#ejercicio_7()

'''
Dado un número entero n, imprimir la suma de los números pares menores o iguales a n
'''
def ejercicio_8():
    # Igual que el 4
    ejercicio_4()
#ejercicio_8()

'''
Dada una lista de números, imprimir la cantidad de números negativos en la lista
'''
def ejercicio_9():
    print(len(list(filter(lambda n : n < 0, hardcoded_numbers))))
#ejercicio_9()

'''
Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.
'''
def ejercicio_10():
    print(list(filter(lambda w : w[0].lower() == w[-1].lower(), hardcoded_words)))
#ejercicio_10()

'''
Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n
'''
def ejercicio_11():
    n = int(input('Ingresar un número:\n'))
    is_prime = lambda n : list(filter(lambda x: (n > 2 and n % x != 0), range(2, int(n**0.5) + 1)))
    print(list(filter(lambda num : is_prime(num), range(2, n+1))))
#ejercicio_11()

'''
Dada una lista de números, imprimir la cantidad de números pares en la lista
'''
def ejercicio_12():
    print(len(list(filter(lambda n : n % 2 == 0, hardcoded_numbers))))
#ejercicio_12()

'''
Dada una lista de palabras, imprimir las palabras que tienen una longitud impar
'''
def ejercicio_13():
    print(list(filter(lambda w : len(w) % 2 != 0,hardcoded_words)))
#ejercicio_13()

'''
Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n
'''
def ejercicio_14():
    def is_perfect(n):
        divisors = 0
        for i in range(1, n):
            if n % i == 0:
                divisors = divisors + i
        return divisors == n
    
    number = int(input('Ingresar un número:\n'))
    print(list(filter(lambda n : is_perfect(n), range(1, number))))
#ejercicio_14()

'''
Dada una lista de números, imprimir la cantidad de números impares en la lista
'''
def ejercicio_15():
    print(len(list(filter(lambda n : n % 2 != 0, hardcoded_numbers))))
#ejercicio_15()

'''
Dada una lista de palabras, imprimir las palabras que tienen una letra específica
'''
def ejercicio_16():
    specific_letter = input('Ingrese una letra:\n')
    print(list(filter(lambda word : specific_letter in word, hardcoded_words)))
#ejercicio_16()

'''
Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n
'''
def ejercicio_17():
    n = int(input('Ingrese un número:\n'))
    
