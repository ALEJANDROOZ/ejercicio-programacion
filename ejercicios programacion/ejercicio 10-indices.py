'''EJERCICIO 10'''
'''Escribe un prog. que solicite al usuario una palabra y determine si la palabra comienza y termina con la misma letra'''

pal=input('Ingrese palabra: ')
primeraL=pal[0]
ultimaL=pal[-1]
if primeraL==ultimaL:
    print('Son iguales')
else:
    ('No lo son')
