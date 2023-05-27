print('='*30)
numero_rodas = int(input('Digite o numero de rodas do veiculo: '))

if numero_rodas >= 4:
    print('O veiculo possui mais de %d rodas imprima o ticket e pague o pedagio.' % numero_rodas)
if numero_rodas >= 2:
    print('O veiculo possui %d rodas portanto não precisa pagar pedagio.' % numero_rodas)
