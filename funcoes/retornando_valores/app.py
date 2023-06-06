def saudacao(nome):
    return "Olá %s" % nome

sds = saudacao('Jeferson')

print(sds)

def check(m, n):
    if m > n:
        return '%d é maior que %d' % (m, n)
    else:
        return '%d é menor que %d' % (m,n)
verificado = check(10,16)
print(verificado)