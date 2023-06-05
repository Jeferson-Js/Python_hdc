# Crie umprograma que busque por elemento.
lista_itens = ['Tv', 'Sofá', 'Cama', 'Armário', 'Porta']


lista_a = input('Busque por um item da lista: ')
econtrado = False

# O método de loop precisa ser i for!
for lista in lista_itens:
    if lista == lista_a:
        print("O item %s foi encontrado na lista" % lista)
        econtrado = True
if econtrado == False:
    print("O item %s não foi encontrado na lista" % lista_a)
    econtrado = False

