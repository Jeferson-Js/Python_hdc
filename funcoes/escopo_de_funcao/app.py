variavel_global = 'Sou global' 

def teste():
    teste = 'Variavel local'
    print(teste)
    print(variavel_global)

teste()

variavel_global = 'quebrou o código'

print(variavel_global)