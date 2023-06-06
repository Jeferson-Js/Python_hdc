class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def normal(self):
        print('Sou uma pessoa normal!')

class Heroi(Pessoa):
    def __init__(self,nome, idade, poderes):
        super().__init__(nome, idade)
        self.poderes = poderes

    def utilizar_super_poderes(self):
        print('O heroi utilizou o %s ' % self.poderes)

jeferson = Pessoa('Jeferson', 30)
jeferson.normal()

jhon = Heroi('Homem', 30, 'soltar teia')
jhon.utilizar_super_poderes()