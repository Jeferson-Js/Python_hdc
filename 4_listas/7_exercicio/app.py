# Crie uma lista de 1 a 10
lista = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

print(lista)

# percorra uma lista com um loop
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

del lista[3]

print(lista)