palavra = 'testando'
print(palavra.upper())

palavra = 'testando'
print(palavra.lower())

user = input('Digite alguma coisa: ')

if user.isupper():
    print('A %s esta em maiuscula' % user)
else:
    print('A %s esta em minuscula' % user)
