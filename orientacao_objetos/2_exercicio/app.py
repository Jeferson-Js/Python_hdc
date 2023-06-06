class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastece(self, litros):
        if self.tanque >= 100:
            print('O tanque esta cheio!')
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque -= (km / km_por_litro)
        

bmw = Carro('BMW', 10000, 4, 100)

print(bmw.tanque)
bmw.dirigir(100)
print(bmw.tanque)
bmw.dirigir(90)
print(bmw.tanque)

# print('A marca do carro é %s ' % (bmw.marca))
# print('O valor do carro é R$ %d ' % (bmw.valor))
# print('O carro tem tem %d portas!' % (bmw.portas))
# print('O carro tem tanque gasolina {} '.format(bmw.tanque_gasolina))

