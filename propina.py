cuenta_total = int(input("Ingrese el monto total de la cuenta: "))
porcentaje_de_propina = int(input("Ingrese el porcentaje de propina que va a dejar: "))

if cuenta_total <= 0:
    print("Error: Ingrese un precio válido.")
    exit()

if porcentaje_de_propina <= 0:
    print("Error: Ingrese un porcentaje válido.")
    exit()

propina_total = (porcentaje_de_propina / 100) * cuenta_total

print(f"Usted va a dejar ${propina_total:.2f} de propina.")
