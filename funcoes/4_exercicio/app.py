def lista_par(lista):
    nova_lista = []
    for numero in lista:
        if numero % 2 == 0:
            nova_lista.append(numero)
    return nova_lista
l_lista = [1,2,3,4,5,6,7,8,9,10]

lista_p = lista_par(l_lista)

print(lista_p)

lista_2 = [25,65,88,7458,658,445,84745,54574]

print(lista_par(lista_2))