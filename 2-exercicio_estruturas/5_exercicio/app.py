salario = float(input('Digite o seu salário: '))

if salario > 1800:
    print('Seu salario é de R$ %.2f reais portanto precisa fazer o imposto de renda. ' % salario)
else:
    print('Seu salário é de R$ %.2f reais portanto não precisa fazer o imposto de renda.' % salario)
