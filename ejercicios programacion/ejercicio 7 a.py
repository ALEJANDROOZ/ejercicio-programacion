'''Ejercicio 7 a'''
'''Escribe un programa que solicite al usuario dos numeros enteros y determine si la suma de ambos es par'''

num1=int(input('Ingrese primer numero: '))
num2=int(input('Ingrese segundo numero: '))
sum=num1+num2
if sum %2==0:
    print('Es par')
else:
    print('No es par')
    