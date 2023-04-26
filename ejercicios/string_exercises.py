'''
1. Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
'''
def ejercicio_1(word):
    return word.upper()
#print(ejercicio_1('hola mundo'))

'''
2. Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
'''
def ejercicio_2(word):
    return word.lower()
    print(input('Ingrese una palabra:\n').lower())
#print(ejercicio_2('HOLA MUNDO'))

'''
3. Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
'''
def ejercicio_3(word_a, word_b):
    return word_a + ' ' + word_b
#print(ejercicio_3('Hola', 'Mundo'))

'''
4. Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
'''
def ejercicio_4(word):
    return len(word)
#print(ejercicio_4('Hola mundo'))

'''
5. Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
'''
def ejercicio_5(word, char):
    return len(list(filter(lambda c : c == char, list(word))))
#print(ejercicio_5('Hola mundo', 'o'))

'''
6. Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
'''
def ejercicio_6(word, char):
    return list(filter(lambda w : char in w, word.split(' ')))
#print(ejercicio_6('Hola estimado mundo, un placer conocerlo', 'o'))

'''
7. Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
'''
def ejercicio_7(word):
    return word.replace(' ', '')
#print(ejercicio_7('Str   i n        g    '))

'''
8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido,
    eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
'''
def ejercicio_8(name, lastname):
    return {
        'name': name.strip().capitalize(),
        'lastname': lastname.strip().capitalize()
    }
#print(ejercicio_8('  Pomelo ', '  morita  '))

'''
9. Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea,
    por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
'''
def ejercicio_9(names):
    return '\n'.join(names)
#print(ejercicio_9(["Juan", "María", "Pedro"]))

'''
10. Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
'''
def ejercicio_10(name, lastname):
    return f'{name[0].lower()}.{lastname.lower()}@utn-fra.com.ar'
#print(ejercicio_10('Andres', 'Caballero'))

'''
11. Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas e "y" antes de la última palabra.
    Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
'''
def ejercicio_11(words):
    return (', '.join(words)[::-1].replace(',', 'y ', 1))[::-1]
#print(ejercicio_11(["manzanas", "naranjas", "bananas"]))


'''
12. Escribir una función que tome un número de tarjeta de crédito como input,
    verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos
    y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
'''
def ejercicio_12(credit_card_number):
    return credit_card_number.replace(' ', '').isnumeric() and f'**** **** **** {credit_card_number[-4:]}' or 'Invalid credit card number'
#print(ejercicio_12('1111 2222 3333 4444'))

'''
13. Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
'''
def ejercicio_13(email):
    return email.split('@')[0]
#print(ejercicio_13('usuario@gmail.com'))

'''
14. Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
'''
def ejercicio_14(url):
    return url.split('.')[1]
#print(ejercicio_14('https://www.ejemplo.com.ar/pagina1'))

'''
15. Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos,
    eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.
'''
def ejercicio_15(word):
    return ''.join(list(filter(lambda c: not c.isdigit(), list(word))))
#print(ejercicio_15('H0l4, m4nd0!'))

'''
16. Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra,
por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
'''
def ejercicio_16(word):
    return ''.join([c[0] for c in word.split(' ')])
#print(ejercicio_16('Universidad Tecnológica Nacional Facultad Regional Avellaneda'))

'''
17. Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits,
    rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
'''
def ejercicio_17(binary):
    return binary.zfill(8)
#print(ejercicio_17('101'))

'''
18. Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas,
por ejemplo: "HoLa" -> "hOlA"
'''
def ejercicio_18(word):
    return word.swapcase()
#print(ejercicio_18('HoLa'))

'''
19. Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
'''
def ejercicio_19(word):
    return len(''.join(list(filter(lambda c: c.isdigit(), list(word)))))
#print(ejercicio_19('1234 Hola Mundo'))

'''
20. Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma,
    por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
'''
def ejercicio_20(emails):
    return ';'.join(emails)
#print(ejercicio_20(["juan@gmail.com", "maria@hotmail.com"]))

'''
21. Crear una función que reciba como parámetro un string y devuelva un diccionario
    donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
'''
def ejercicio_21(sentence):
    words_count = {}
    for word in sentence.split(' '):
        if word in words_count.keys():
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count

#print(ejercicio_21('Pomelo vive con Morita, y ahora Morita y Pomelo viven con Uva'))    