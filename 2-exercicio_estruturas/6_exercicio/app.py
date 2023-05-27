n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 * n2

if soma <= 100:
    print('O valor digitado foi  %d e é baixo!' % soma)
elif soma >= 100:
    print('O valor digitado foi %d e é um número alto ' % soma)
else:
    print('O valor digitado foi %d e é igual portanto não é maior nem menor!')