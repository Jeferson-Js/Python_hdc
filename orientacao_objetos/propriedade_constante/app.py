class Carro:

    rodas = 4

    def __init__(self, marca):
        self.marca = marca

bmw = Carro('BMW')

print(bmw.marca)
print(bmw.rodas)