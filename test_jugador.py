def test_dar_ficha():
    j = Jugador("Andres",10)
    j.darFicha(5)
    assert(j.fichas==15)