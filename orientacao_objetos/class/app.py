class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
pessoa = Pessoa('Jeferson', 30)
print(pessoa.name)
print(pessoa.age)

if pessoa.name == 'Jeferson':
    print('Seu nome é ' + pessoa.name)