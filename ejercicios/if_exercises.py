from math import sqrt

'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número ingresado es positivo" si el número es mayor que cero,
o "El número ingresado es cero o negativo" si el número es menor o igual a cero.
'''
def ejercicio_1():
    print(int(input('Ingresar un número:\n')) > 0 and 'El número ingresado es positivo' or 'El número ingresado es cero o negativo')

#ejercicio_1()

'''
Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18,
o "Eres menor de edad" si la edad es menor a 18.
'''
def ejercicio_2():
    print(int(input('Ingrese su edad:\n')) >= 18 and 'Eres mayor de edad' or 'Eres menor de edad')

#ejercicio_2()

'''
Escribir un programa que le pida al usuario que ingrese un número entero, 
y luego imprima "El número ingresado es par" si el número es divisible por 2,
o "El número ingresado es impar" si el número no es divisible por 2.
'''
def ejercicio_3():
    print(int(input('Ingrese un número:\n')) % 2 == 0 and 'El número ingresado es par' or 'El número ingresado es impar')

#ejercicio_3()

'''
Escribir un programa que le pida al usuario que ingrese dos números enteros,
y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo,
"El segundo número es mayor" si el segundo número es mayor que el primero,
o "Los dos números son iguales" si los dos números son iguales.
'''
def ejercicio_4():
    a, b = int(input('Ingrese un número:\n')), int(input('Ingrese otro número:\n'))
    print ('Los dos números son iguales' if a == b else 'El primer número es mayor' if a > b else 'El segundo número es mayor')

#ejercicio_4()

'''
Escribir un programa que le pida al usuario que ingrese su nombre,
y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", 
o "Hola desconocido" si el nombre ingresado no es uno de esos tres.
'''
def ejercicio_5():
    name = input('Ingrese su nombre:\n')
    print(name in ['Juan', 'María', 'Pedro'] and f'Hola {name}'or 'Hola desconocido')
    
#ejercicio_5()

'''
Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
y luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o igual a 65,
o "No puedes votar" si la edad es menor a 18 o mayor a 65.
'''
def ejercicio_6():
    name, age = input('Ingrese un nombre:\n'), int(input('Ingrese una edad:\n'))
    print(f'El ciudadano {name} ' + (age >= 18 and age <= 65 and 'si' or 'no') + ' puede votar')

#ejercicio_6()

'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.
'''
def ejercicio_7():
    n = int(input('Ingrese un número:\n'))
    print(list(filter(lambda x: (n % x == 0), range(2, n))) and 'El número no es primo' or "El número es primo")
    
#ejercicio_7()

'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto,
o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.
'''
def ejercicio_8():
    r = sqrt(int(input('Ingrese un número:\n')))
    print(r == int(r) and 'El número es un cuadrado perfecto' or 'El número no es un cuadrado perfecto')

#ejercicio_8()

'''
Escribir un programa que le pida al usuario que ingrese una letra,
y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u),
o "Es una consonante" si la letra es una consonante.
'''
def ejercicio_9():
    print(input('Ingrese una letra:\n').lower() in ['a', 'e', 'i', 'o', 'u'] and 'Es una vocal' or 'Es una consonante')

#ejercicio_9()

'''
Escribir un programa que le pida al usuario que ingrese un número entero, 
y luego imprima "El número es positivo y par" si el número es positivo y divisible por 2, 
o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores.
'''
def ejercicio_10():
    n = int(input('Ingrese un número:\n'))
    print(n > 0 and n % 2 == 0 and 'El número es positivo y par' or 'El número no cumple ninguna condición')

#ejercicio_10()

'''
Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres un niño" si la edad es menor a 12, 
"Eres un adolescente" si la edad está entre 12 y 17 inclusive,
"Eres un adulto" si la edad está entre 18 y 64
'''
def ejercicio_11():
    n = int(input('Ingrese un número\n'))
    m = 'Sos un abuelo'
    if (n >= 18 and n <= 64):
        m = 'Eres un adulto'
    elif (n >= 12 and n <= 17):
        m = 'Eres un adolescente'
    elif (n < 12):
        m = 'Eres un niño, cuidado con Telefe'
    print(m)

#ejercicio_11()

'''
Escribir un programa que le pida al usuario que ingrese dos números enteros, 
y luego imprima "El primer número es positivo" si el primer número es mayor que cero, 
"El segundo número es positivo" si el segundo número es mayor que cero, 
o "Ambos números son negativos" si los dos números son negativos.
'''
def ejercicio_12():
    a = int(input('Ingrese un número:\n'))
    b = int(input('Ingrese otro número:\n'))
    if (a > 0):
        print('El primer número es positivo')
    if(b > 0):
        print('El segundo número es positivo')
    if(a < 0 and b < 0):
        print('Ambos son negativos')

#ejercicio_12()

'''
Escribir un programa que le pida al usuario que ingrese un número entero, 
y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 y por 5, 
o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.
'''
def ejercicio_13():
    n = int(input('Ingrese un número:\n'))
    print(n % 3 == 0 and n % 5 == 0 and 'El número es divisible por 3 y por 5' or 'El número no es divisible por 3 y por 5')

#ejercicio_13()

'''
Escribir un programa que le pida al usuario que ingrese un número entero, 
y luego imprima "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, 
o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.
'''
def ejercicio_14():
    n = int(input('Ingrese un número:\n'))
    print(n % 4 == 0 and n % 6 == 0 and 'El número es múltiplo de 4 y de 6' or 'El número no es múltiplo de 4 y de 6')

#ejercicio_14()