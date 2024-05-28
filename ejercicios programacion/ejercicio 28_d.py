rent=int(input('Ingrese su renta Anual: '))

if rent<10000:
         print ('5%')
elif rent>=10000 and rent <20000:
         print ('15%')
elif rent>=20000 and rent<35000:
         print('20%')
elif rent>35000 and rent<60000:
    print('30%')
elif rent>60000:
    print ('45%')