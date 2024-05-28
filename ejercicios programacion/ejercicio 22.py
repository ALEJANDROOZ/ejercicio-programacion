#entrada
apellido = input("Por favor, ingrese su apellido: ")
nombre = input("Por favor, ingrese su nombre: ")

#proceso
mail = apellido.lower() + "_" + nombre.lower() + "@tdf.edu.ar"

#salida
print("-" * 100)
print("Su mail generado automáticamente es: " + mail)