Nombre = input("Escriba su nombre :")

nombre_minus = Nombre.lower()
nombre_mayus = Nombre.upper()
nombre_capital = Nombre.title()
nombre_cont = Nombre.replace(" ", "")

print(nombre_minus)
print(nombre_mayus)
print(nombre_cont)
print(nombre_capital)

letra_a_consultar = input("Ingrese una letra para buscar en el nomre :")
letra_consultada = letra_a_consultar.find()
print(letra_consultada)
