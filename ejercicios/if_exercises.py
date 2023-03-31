
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

