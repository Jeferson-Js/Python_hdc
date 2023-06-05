nomes = ['Jeferson', 'Santos', 'Oliveira']

i = 0 

itens_econtrados = input('Digite um objeto: ')
achou = False

while i < len(nomes):
    if nomes[i] == itens_econtrados:
        print("Encontramos um %s " % itens_econtrados)
        achou == True
        i += 1
if achou == False:
    print("Não encontramos o objeto %s " % itens_econtrados)