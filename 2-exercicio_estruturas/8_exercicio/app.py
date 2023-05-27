print('='*5)
categoria = int(input('Digite um valor númerico: '))

if categoria == 1:
    print('O valor %d é uma bolsa' % categoria)
elif categoria == 2:
    print('O valor %d é um tênis' % categoria)
elif categoria == 3:
    print('O valor %d é uma mochila' % categoria)
else:
    print('O valor digitado não corresponde a nunhuma categoria.')