while True:
    try:
        cantidad_de_comensales = int(input("Ingrese la cantidad de personas en numeros:"))
        if cantidad_de_comensales <= 0:
            raise ValueError("La cantidad de personas debe de ser ingresada en numeros")
        break
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un valor válido.")
try:
    cuenta_total = float(input("Ingrese el monto total de la cuenta : "))
    if cuenta_total == 0:
        raise ValueError("El monto total debe de ser mayor a 0")
    porcentaje_de_propina = int(input("Ingrese el porcentaje de propina que va a dejar : "))
    if porcentaje_de_propina <= 5:
        raise ValueError("El porcentaje de propina debe de ser mayor a 5%")
    propina_total = (porcentaje_de_propina / 100) * cuenta_total
    print(f"Usted va a dejar ${propina_total: .2f}de propina" )
    calcular_diferencia_por_persona = input("¿Quiere calcular cuánto debería poner cada persona? (si/no): ").strip().lower()
    if calcular_diferencia_por_persona == "si":
        cuenta_propina = propina_total / cantidad_de_comensales
        cuenta_general = (cuenta_total / cantidad_de_comensales) + cuenta_propina
        print(f"Cada persona debe abonar: ${cuenta_general:.2f} (incluye la propina).")
    elif calcular_diferencia_por_persona == "no":
        print("Espero que hayan disfrutado de la comida.")
    else:
        print("Por favor, ingrese una respuesta válida.")
except ValueError as e:
    print(f"Error: {e}. Por favor, revise los datos ingresados.")

finally:
    print("Gracias por usar el programa.")