'''EJERCICIO 5- Escribe un programa que solicite al usuario su nombre y determine si su nombre empieza con una vocal (A E I O U)'''

nombre=input('Ingrese su nombre: ')
primeraL=nombre[0]

if primeraL in 'aeiou':
    print('Empieza en vocal: ',nombre[0])
else:
    print('No empieza en vocal...')
