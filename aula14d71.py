#funcionamento de um caixa eletronico
#perguntar o valor sacado
#calcular quantas celulas serao entregues
#valor das celulas: 1,10,20,50

import math

while True:

    valor = float(input('Valor a ser sacado: R$ '))

    notas50 = valor/50
    r = valor%50

    notas20 = r/20
    r = valor%20

    notas10 = r/10
    r = valor%10

    notas1 = r

    if valor < 10:
        notas1 = valor
    break

if notas50 >= 1:
    print('Total de notas de 50: {:.0f}'.format(math.floor(notas50)))
if notas20 >= 1:
    print('Total de notas de 20: {:.0f}'.format(math.floor(notas20)))
if notas10 >= 1:
    print('Total de notas de 10: {:.0f}'.format(math.floor(notas10)))
if notas1 >= 1:
    print('Total de notas de 1: {:.0f}'.format(math.floor(notas1)))