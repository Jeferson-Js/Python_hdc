valor = int(input('Digite um valor: '))

if valor > 10:
    if valor > 20:
        print('O número é maior que vinte 20')
        print(valor * 2)
    else:
        print('O número é menor que 20')
        print(valor * 5)
else:
    print('O valor digitado é %d é maior que 10 pode proseguir' % valor)

