import pytest
from apuesta import Apuesta

# Test para el constructor __init__
def test_inicializacion():
    apuesta = Apuesta()
    assert apuesta.fichas == 0, "La apuesta debería comenzar con 0 fichas"
    assert apuesta.estaVacia(), "La apuesta debería estar vacía al inicio"

# Test para ponerFicha con el valor por defecto
def test_poner_ficha_default():
    apuesta = Apuesta()
    apuesta.ponerFicha()
    assert apuesta.fichas == 1, "Debería haber 1 ficha después de agregar una"

# Test para ponerFicha con una cantidad específica
def test_poner_ficha_cantidad():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert apuesta.fichas == 5, "Debería haber 5 fichas después de agregar 5"

# Test para tomarFicha con una cantidad específica
def test_tomar_ficha():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    apuesta.tomarFicha(3)
    assert apuesta.fichas == 2, "Debería haber 2 fichas después de tomar 3"

# Test para tomarFicha lanzando un error al intentar tomar más fichas de las disponibles
def test_tomar_ficha_exceso():
    apuesta = Apuesta()
    apuesta.ponerFicha(2)
    try:
        apuesta.tomarFicha(3)
    except ValueError:
        pass  # Correcto, debería lanzar un ValueError
    else:
        assert False, "Debería lanzar un ValueError al intentar tomar más fichas de las disponibles"

# Test para tomarTodas
def test_tomar_todas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    cantidad = apuesta.tomarTodas()
    assert cantidad == 5, "Debería haber tomado 5 fichas"
    assert apuesta.fichas == 0, "La apuesta debería estar vacía después de tomar todas las fichas"

# Test para tieneFicha
def test_tiene_ficha():
    apuesta = Apuesta()
    apuesta.ponerFicha(3)
    assert apuesta.tieneFicha(2), "Debería tener al menos 2 fichas"
    assert not apuesta.tieneFicha(4), "No debería tener 4 fichas"

# Test para estaVacia
def test_esta_vacia():
    apuesta = Apuesta()
    assert apuesta.estaVacia(), "Debería estar vacía al inicio"
    apuesta.ponerFicha(1)
    assert not apuesta.estaVacia(), "No debería estar vacía después de poner fichas"

# Ejecutar los tests
if __name__ == "__main__":
    test_inicializacion()
    test_poner_ficha_default()
    test_poner_f
