import random
numero_aleatorio = random.randrange(1, 101)
Adivinar = int(input("Ingrese un numero entre el 1 y el 100 :"))
intentos = 0
while True :
    intentos += 1
    if Adivinar < 0:
        print("Elije un numero positivo")
    elif Adivinar > 100:
        print("Elije un numero mas pequeño")
    elif Adivinar == numero_aleatorio:
        print(f"Muy bien has adivinado el numero, en {intentos} intentos")
        break
    elif Adivinar < numero_aleatorio:
        print("El numero es mas grande")
    else:
        print("El numero es mas pequeño")
    print(f"Intento N {intentos}")
    Adivinar = int(input("Intenta de nuevo :"))
