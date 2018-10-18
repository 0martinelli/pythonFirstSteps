#programa que le numeros inteiros, mostra sua média o maior número e o menor número lido.
parar = False
soma = 0
maior = 0
menor = 0
c = 0
while parar == False:

    n = int(input('Digite um número: '))
    c += 1

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    soma += n

    n2 = int(input('Digite 1 para continuar a digitar e 2 para parar: '))
    if n2 == 1:
        parar = False
    else:
        parar = True

media = soma/c

print('Maior {}'.format(maior))
print('Menor {}'.format(menor))
print('Media {}'.format(media))

