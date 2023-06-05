listas = [10,67,88,90,77,20,18]

menor_valor = listas[0]

for lista in listas:
    if lista < menor_valor:
        menor_valor = lista
print(menor_valor)