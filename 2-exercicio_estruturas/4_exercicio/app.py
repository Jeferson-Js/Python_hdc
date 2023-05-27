idade = int(input('Digite a sua idade: '))

if idade > 18:
    print('Você tem %d anos é maior de idade pode entrar' % idade)
elif idade < 18:
    print('Você tem  %d anos é considerado menor de idade portanto precida de autorização dos pais ' % idade)
else:
    print('Infelizmente você não tem idade o suficiente portanto não pode entrar.')