import random

aleatorio = random.randint(1,10)

palpite = input('Adivinhe um número: ') 

if aleatorio == palpite:
    print('Parabéns você acertou o número é %d ' % aleatorio)
else: 
    print('Você errou!! o número era %d ' % aleatorio)

