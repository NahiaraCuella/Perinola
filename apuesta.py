class Apuesta:
    def __init__(self):
        self.fichas = 0

    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas"

    def ponerFicha(self, cuantas=1):
        self.fichas += cuantas

    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No podes sacar más fichas de las que hay apostadas.")
        self.fichas -= cuantas

    def tomarTodas(self):
        cantidad = self.fichas
        self.fichas = 0
        return cantidad

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas

    def estaVacia(self):
        return self.fichas == 0

