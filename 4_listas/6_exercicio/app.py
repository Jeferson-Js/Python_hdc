lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]

print(lista_a)
print(lista_b)

lista_c = []

contador_a = 0

while contador_a < len(lista_a):
    lista_c.append(lista_a[contador_a])
    contador_a += 1

contador_b = 0

while contador_b < len(lista_b):
    lista_c.append(lista_b[contador_b])
    contador_b += 1

    print(lista_c)