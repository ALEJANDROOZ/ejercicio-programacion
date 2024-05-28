hs_t=int(input('Ingrese cantidad de horas: '))
codigo=int(input('Ingrese codigo de Turno: '))
turno_a=5234
turno_b=8057.75
if codigo==1:
    cobro=hs_t*turno_a
    print('Sueldo a Cobrar: ',cobro) 
elif codigo==2:
    cobro=hs_t*turno_b
    print('Sueldo a Cobrar: ',cobro)
else:
    print('Codigo de horas Incorrecto') 
