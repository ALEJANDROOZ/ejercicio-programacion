

tipopizza=int(input('1-Veg y 2 No Veg'))
if tipopizza==1:
     print('Menu Vegetariano')
     print('Pimiento')
     print('Tofu')
     ingrediente= input('Ingrese ingrediente: ')
     if ingrediente=='Pimiento' or ingrediente=='Tofu':
         print('Los ingredientes de su Pizza Vegetariana son: Mozzarella, tomate',ingrediente)
     

else:
    print('Menu no Vegetariano')
    print('Ingredientes')
    print('peperoni')
    print('jamon')
    print('salmon')
    ingrediente=input('Ingrese ingrediente: ')
    if ingrediente=='peperoni' or ingrediente=='jamon' or ingrediente=='salmon':
        print('Pizza no Vegetariana', ingrediente)
        print('Los ingredients de su Pizza NO Vegetariana son:Mozarella, tomate', ingrediente)
       