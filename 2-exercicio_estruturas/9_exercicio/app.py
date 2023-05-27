salario = float(input('Digite o seu salário: '))

if salario <= 2000:
    print('Com base em sua renda salárial que é de R$ %.2f reais o limite liberado foi de 1000' % salario)
elif salario <= 4000:
    print('Com base em sua renda salárial que é de R$ %.2f reais o limite liberado foi de 2000' % salario)
elif salario <= 6000:
    print('Com base em sua renda salárial que é de R$ %.2f reais o limite liberado foi de 3000' % salario)
else:
    print('Com base em sua renda salárial que é de R$ %.2f reais para saber quanto de limite esta disponivel você precisa falar com o gerente da sua conta!' % salario)