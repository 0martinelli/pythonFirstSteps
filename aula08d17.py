#Programa que le o cateto oposto e o adjacente e mostra a hipotenusa

from math import hypot

o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é: {:.2f}'.format(hypot(o, a)))

