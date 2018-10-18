#Le o angulo, mostra o seno, cosseno e tangete deste angulo

from math import sin,cos,tan,radians

n1 = int(input('Digite o angulo desejado: '))

n = radians(n1)

print('O seno do número é {:.2f}, o cosseno é {:.2f} e a tangete é {:.2f}'.format(sin(n),cos(n),tan(n)))