from piedra_papel_tijeras import *
def test_ordenador_decide_jugada():
    eleccion=ordenador_decide_jugada()
    print("El jugador eligió: ", eleccion)
    print()

def test_usuario_decide_jugada():
    eleccion= usuario_decide_jugada()
    print(f"El usuario eligió: {eleccion}")
    print()

def test_determina_ganador(eleccion_jugador, eleccion_ordenador):
    print(f"Jugador: {eleccion_jugador} vs. Ordenador: {eleccion_ordenador}")
    resultado=determina_ganador(eleccion_jugador, eleccion_ordenador)
    print("El resultado es: ", resultado)
    print()


if __name__=="__main__":
    test_usuario_decide_jugada()
    test_ordenador_decide_jugada()
    test_determina_ganador("piedra", "tijeras")
    test_determina_ganador("piedra", "papel")
    test_determina_ganador("piedra", "piedra")
    test_determina_ganador("tijeras", "tijeras")
    test_determina_ganador("tijeras", "papel")
    test_determina_ganador("tijeras", "piedra")
    test_determina_ganador("papel", "tijeras")
    test_determina_ganador("papel", "papel")
    test_determina_ganador("papel", "piedra")