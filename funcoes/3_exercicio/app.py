# # Escreva uma função que receba um dado em texto
# def dadoEmTexto(nome):
#     if len(nome) >= 20:
#         return 'A palavra %s é muito longa! ' % nome
#     else: 
#         return 'A palavra %s é muito curta! ' % nome

# verificado = dadoEmTexto('kkkkjkjkjkjkjksdsdsdsssddsdsdsdsdddswwwewewewewe')

# print(verificado)

palavra = input('Digite uma palavra: ')

def tamanhoDoTexto(texto):
    if len(texto) >= 20:
        return 'A palavra %s é muito grande' % texto
    else:
        return 'A palavra %s é muito curta' % texto

verificado = tamanhoDoTexto(palavra)

print(verificado)