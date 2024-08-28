from random import choice
class Perinola:
    def __init__(self):
        self.texto = "Pon 1"
    def __repr__(self):
        return f"Salio: {self.texto}"
    def tirar(self):
       caras = ("Pon 1", "Toma 2", "Todos Ponen",
       "Toma 1", "Pon 2", "Toma Todo")
       self.texto = choice(caras)
       return self.texto   