class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return 'O nome da pessoa é %s sua idade é %d anos e sua profissão é %s!' % (self.nome, self.idade, self.profissao)

jeferson = Pessoa('Jeferson', 30, 'programador')

    
print(jeferson.__str__())