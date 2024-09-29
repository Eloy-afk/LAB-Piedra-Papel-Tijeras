import random
from time import sleep
opciones=["piedra", "papel", "tijeras"]
contador_user=0
contador_pc=0
while True:
    user=input("Elija: piedra, papel o tijeras: ").lower()
    print()
    print(f"Has seleccionado {user}")
    print()
    sleep(0.8)
    if user not in opciones:
        print("Escriba una opción válida, por fabor.")
        continue
    pc=random.choice(opciones)
    sleep(0.8)
    print(f"El ordenador ha seleccionado: {pc}")
    print()
    if user == pc:
        print(f"Empate, ambos habéis elegido {user}.")
    elif user=="piedra" and pc=="tijeras":
        print(f"¡Ganaste! {user} gana frente a {pc}")
        contador_user+=1
    elif user=="tijeras" and pc=="papel":
        print(f"¡Ganaste! {user} gana frente a {pc}")
        contador_user+=1
    elif user=="papel" and pc=="piedra":
        print(f"¡Ganaste! {user} gana frente a {pc}")
        contador_user+=1
    else:
        print(f"Perdiste! {pc} gana frente a {user}")
        contador_pc+=1
    sleep(0.8)
    print()
    print(f"El usuario tiene: {contador_user} puntos, mientras que el ordenador tiene: {contador_pc} puntos.")
    if contador_user==3:
        print("¡Has ganado, enorabuena!")
    elif contador_pc==3:
        print("Has perdido, gana el ordenador.")
    print("---------------------------------------------------")
    
    
