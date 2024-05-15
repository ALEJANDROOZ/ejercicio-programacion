medfrent=int(input('Ingrese medida Frontal: '))
medprof=int(input('Ingrese medida de fondo: '))
sup=(medfrent*medprof)
perimcuad=(4*medfrent)
perimrect=((2*medfrent)+(2*medprof))
if medfrent==medprof:
    print('Terreno cuadrado')
    print('Su Perimetro es: ',perimcuad)
    print('Su Superficie es: ',sup)
elif medfrent!=medprof:
    print('Terreno Rectangular')
    print('Su perimetro es: ',perimrect)
    print('Su Superficie es: ',sup)
