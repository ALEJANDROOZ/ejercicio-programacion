'''Escriba un programa que solicite al usuario un numero entero y determine si el numero es multiplo de 3 y multiplo de 5'''

a=int(input('Ingrese numero: '))
if a%3==0 and a%5==0:
    print('Numero divisible por 3 y por 5')
else:
    print('No divisible por 3 y por 5')