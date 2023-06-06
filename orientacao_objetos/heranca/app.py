class Veiculo:
    def __init__(self, marca, rodas):
        self.marca = marca
        self.rodas = rodas

    def ligar(self):
        print('Veiculo ligado!!')

class Moto(Veiculo):
    def __init__(self,marca,rodas, bag):
        super().__init__(marca,rodas)
        self.bag = bag

kawazaki = Moto('BMW', 2, True)

print('O modelo da moto é %s' % kawazaki.marca)
print('O número de rodas é %d' % kawazaki.rodas)
print('A moto tem bag? %s' % kawazaki.bag)

kawazaki.ligar()
