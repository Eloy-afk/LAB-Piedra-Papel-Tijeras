import random
def ordenador_decide_jugada():
    opciones=["piedra", "papel", "tijeras"]
    res= random.choice(opciones)
    return res

def usuario_decide_jugada():
    eleccion_usuario=input("Elige piedra, papel o tijeras: ")
    return eleccion_usuario


def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"