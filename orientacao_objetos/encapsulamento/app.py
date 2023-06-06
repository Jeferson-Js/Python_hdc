class Aviao:
    __asas = 2

    def __init__(self, marca):
        self.marca = marca

    def asa_aviao(self):
        print('O aviao tem %d asas' % (self.__asas))

aviao = Aviao('Avião Oliveira.js')

print(aviao.marca)

aviao.asa_aviao()