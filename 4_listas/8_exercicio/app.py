# Crie uma lista com alguns itens
print('='*10 + " Lista de Itens " + '='*10)
lista_itens = ['Sofá', 'Cama', 'Mesa', 'Tv', 'Geladeira']
print(lista_itens)

# Peça 2 itens ao usuario

item_a = input('Digite um item da lista: ')
item_b = input('Digite um item da lista: ')
achou = False

i = 0

while i < len(lista_itens):
    if lista_itens[i] == item_a:
        print("O item %s foi econtrado na lista  A ! " % item_a)
        achou == True
        break
    elif lista_itens[i] == item_b:
        print("O item %s foi econtrado na lista  B ! " % item_b)
        achou == True
        break
    i += 1

if achou == False:
    print("Não foi encontrado o item %s na lista A e B " % lista_itens)
    achou == False
