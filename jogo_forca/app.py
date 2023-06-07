from palavras import palavras
import random

# Selecione a palavra
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

teste = selecionar_palavra()
print(teste)
