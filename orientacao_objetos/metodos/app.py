class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saudacao(self):
        print('Olá programador!')
jeferson = Pessoa('Jeferson', 30)

print("Seu nome é %s " % jeferson.name)
print("Sua idade atual é %d " % jeferson.age)

jeferson.saudacao()