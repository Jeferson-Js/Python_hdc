salario = float(input('Digite seu salário: '))
aumento = int(input('Digite quanto quer de aumento: '))

novo_salario = salario + (salario * (aumento/100))

print('%.2f' % novo_salario)