'''EJERCICIO 9'''
'''Escriba un prog. que solicite al usuario un año y determine si es bisiesto.
Dato: un año es bisiesto si es divisible por 4, pero no por 100 a menos que tambien sea divisible por 400'''

año=int(input('Ingrese el año: '))
if año % 4 ==0:
    print('Año Bisiesto')
else:
    print('Año no Bisiesto')