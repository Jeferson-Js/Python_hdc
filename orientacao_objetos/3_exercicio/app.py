class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
# Aqui realizamos o metodo de saque!
    def saque(self, valor):
        self.saldo -= valor
# Aqui realizamos o metodo de deposito
    def deposito(self, valor):
        self.saldo += valor 
# Aqui realizamos o metodo de trânsferencia entre contas
    def trânsferencia(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor

jeferson = Banco('Jeferson', 1000)

print('O titular da conta é  %s ' % jeferson.nome)
print('Seu saldo é %s ' % jeferson.saldo)

jeferson.saque(100)
print('Seu saldo anterior é de %s ' % jeferson.saldo)

jeferson.deposito(200)
print('Seu saldo atual é de %s ' % jeferson.saldo)

conta_maria = Banco('Maria', 100)

jeferson.trânsferencia(conta_maria, 500)

print(conta_maria.saldo)