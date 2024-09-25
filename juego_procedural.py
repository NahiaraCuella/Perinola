from random import choice

fichas = [5, 5, 5, 5]
nombres = ["j1", "j2", "j3", "j4"]
apuesta = 0
tiro = "Pon 1"

def tirarPerinola():
    caras = ("Pon 1", "Toma 2", "Todos Ponen",
     "Toma 1", "Pon 2", "Toma Todo")
    return choice(caras)

def ponerTodos():
    global apuesta
    print("Ponen todos")
    for i in range(len(fichas)):
        fichas[i] = fichas[i]-1
        apuesta = apuesta + 1

def mostrarApuesta():
    print(f"apuesta: {apuesta}")

def mostrarJugadores():
    for i in range(len(fichas)):
        print(f"{nombres[i]}: {fichas[i]}")

def mostrarAQuienLeToca():
    print(f"Le toca a {nombres[0]}")

def sacarPerdedores():
    global turno
    a_sacar = []
    for i in range(0, len(fichas)):
        if fichas[i] == 0:
            a_sacar.append(i)
    for i in reversed(a_sacar):
        fichas.pop(i)
        n = nombres.pop(i)
        print(f"Perdió {n}")

def pasarTurno():
  f = fichas.pop(0)
  fichas.append(f)
  n = nombres.pop(0)
  nombres.append(n)

def quedaUnSoloJugador():
  return (len(fichas) == 1)

## Programa Principal

ponerTodos()

while not quedaUnSoloJugador():
    mostrarJugadores()
    mostrarApuesta()

    if apuesta == 0:
        ponerTodos()
    sacarPerdedores()

    if quedaUnSoloJugador():
        break

    mostrarAQuienLeToca()
    tiro = tirarPerinola()
    print(tiro)

    if tiro == "Pon 1":# from random import randint
        fichas[0] = fichas[0] - 1
        apuesta = apuesta + 1
    elif tiro == "Pon 2":
        if fichas[0] < 2:
            apuesta = apuesta + fichas[0]
            fichas[0] = 0
        else:
            fichas[0] = fichas[0] - 2
            apuesta = apuesta + 2
    elif tiro == "Toma 1":
        fichas[0] = fichas[0] + 1
        apuesta = apuesta - 1
    elif tiro == "Toma 2":
        if apuesta < 2:
            fichas[0] = fichas[0] + apuesta
            apuesta = 0
        else:
            fichas[0] = fichas[0] + 2
            apuesta = apuesta - 2
    elif tiro == "Toma Todo":
        fichas[0] = fichas[0] + apuesta
        apuesta = 0
    elif tiro == "Todos Ponen":
        ponerTodos()

    mostrarJugadores()
    sacarPerdedores()
    pasarTurno()
    print()

print(f"Terminó el juego, ganó: {nombres[0]}")