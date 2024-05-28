'''EJERCICIO 3- Escribe un programa que solicite al usuario un numero entero
y determine si el numero NO esta dentro de 1 y 100 (inclusive)'''


a=int(input('Ingrese numero: '))

if not 1>a and a<100:
      print('El numero es correcto: Se encuentra entre 0 y 100')
else:
    print('Algun numero incorrecto: Esta fuera del rango entre 0 y 100')
    
''' Solucion sin usar not 0<a<=100'''