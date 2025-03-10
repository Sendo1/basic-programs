
cantidad_de_comensales = int(input("Ingrese la cantidad de personas en numeros:"))
if cantidad_de_comensales <= 0:
    print("Ingrese una respuesta valida")
    exit()
cuenta_total = float(input("Ingrese el monto total de la cuenta : "))
porcentaje_de_propina = int(input("Ingrese el porcentaje de propina que va a dejar : "))

if cuenta_total <= 0:
    print("ingrese un precio valido")
    exit()
    
if porcentaje_de_propina <=0:
    print("ingrese un porcentaje valido")
    exit()
propina_total = (porcentaje_de_propina / 100) * cuenta_total

print(f"Usted va a dejar ${propina_total: .2f} de propina" )
calcular_diferencia_por_persona = str(input("Quires calcular cuanto deberia de poner cada persona? (si/no) :")).lower()

if calcular_diferencia_por_persona == "si":
    cuenta_propina = propina_total / cantidad_de_comensales
    cuenta_general = (cuenta_total / cantidad_de_comensales) + cuenta_propina
    print(f"Lo que debe abonar cada uno por la cuenta y propina es :{cuenta_general}")
elif calcular_diferencia_por_persona == "no":
    print("Espero que hayan disfrutado de la comida")
else:
    print("Ingrese una respuesta valida")
    