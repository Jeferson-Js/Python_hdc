notas = [10,10,10,10,10]
print(notas)

i = 0
soma = 0
aprovado = 9

while i < 5:
    soma = soma + notas[i]
    i += 1
    media = soma / 5

if media > aprovado:
    print('O aluno teve a nota %.1f e esta aprovado no exame! ' % media)
else:
    print('O aluno não foi aprovado sua nota foi %.1f esta abaixo do pedido! ' % media)
