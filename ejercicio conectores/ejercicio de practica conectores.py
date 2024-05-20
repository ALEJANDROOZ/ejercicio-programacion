'''Ejercicio de practica: Conectores'''

'''ejercicio 1- Escribir un programa que solicite al usuario
dos numeros enteros y determine si ambos numeros son mayores a 10'''

'''EJERCICIO 2- Escriba un programa que solicite al usuario dos numeros
enteros y determine si al menos uno de ellos es par'''

'''EJERCICIO 3- Escribe un programa que solicite al usuario un numero entero
y determine si el numero NO esta dentro de 1 y 100 (inclusive)'''

'''EJERCICIO 1- SOLUCION'''

a=int(input('Ingrese primer numero: '))
b=int(input('Ingrese segundo numero: '))
if a<10 and b<10:
    print('Numeros correctos')
else:
    print('Alguno incorrecto: Mayor a 10' )
    
'''EJERCICIO 2- SOLUCION'''

a=int(input('Ingrese primer Numero: '))
b=int(input('Ingrese segundo Numero: '))
if a%2==0 and b%2==0:
    print('Numeros pares')
else:
    print('Algun numero es impar')


    



