def cal_media(lista):
    media = 0
    soma = 0

    for nota in lista:
        soma += nota

    media = soma / len(lista)

    return media

notas = [9,8,7]

media_notas = cal_media(notas)

print(media_notas)