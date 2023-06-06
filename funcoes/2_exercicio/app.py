def maiorOuMenor(a, b):
    if a > b:
        return "O número %d é maior que %d" % (a, b)
    else:
        return "O número %d é menor que %d" % (a, b)
verificado = maiorOuMenor(5,10)

print(verificado)