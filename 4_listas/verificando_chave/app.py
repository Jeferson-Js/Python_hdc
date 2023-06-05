pessoa = {
    'nome': 'Jeferson',
    'idade': 30,
    'cidade': 'São Paulo'
}

print(pessoa)

print('nome' in pessoa)
print('idade' in pessoa)
print('cidade' in pessoa)

if 'nome' in pessoa:
    print('Seu nome é %s' % pessoa['nome'])
else:
    print('Esta pessoa não esta cadastrada no sistema')