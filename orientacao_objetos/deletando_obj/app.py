class Pessoa:
    def __init__(self, name):
        self.name = name


jeferson = Pessoa('Jeferson')
carol = Pessoa('Carol')

print(jeferson.name)
print(carol.name)

del jeferson
del carol

print(jeferson.name)
print(carol.name)