class Carro:
    def __init__(self, portas, motor, teto, preco):
        self.portas = portas
        self.motor = motor
        self.teto = teto
        self.preco = preco

bmw = Carro(4, 1, True, 5000)

print("O carro tem: %d " % bmw.portas)
