roupas = ['Camisa', 'preta', 25.00]
blusa = ['Blusa', 'marrom', 35.00]

produtos = [roupas, blusa]

print(produtos)

for produto in produtos:
    print("O nome do produto é %s sua cor é %s seu preço é R$ %.2f " % (produto[0], produto[1]))
