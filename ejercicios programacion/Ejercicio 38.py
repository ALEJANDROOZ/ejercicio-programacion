#Ejercicio 38
sumpositivo=0
num= int (input('Ingrese numero: '))
while num!=0:
    if num>0:
      sumpositivo += num
    num =int(input('Ingrese numero: '))
print('La sumatoria total es: ',sumpositivo)