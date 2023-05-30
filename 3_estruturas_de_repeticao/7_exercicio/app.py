def is_prime(number):
    if number < 2:
        return False
    contador = 2
    while contador <= int(number ** 0.5):
        if number % contador == 0:
            return False
        contador += 1
    return True

num = int(input('Digite um número inteiro: '))

if is_prime(num):
    print('O número %d é primo ' % num)
else:
    print('O número %d não é primo ' % num)