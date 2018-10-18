# fazer o usuario acertar um numero randomico gerado pelo computador
import random

print('Computador gerando um número aleatório entre 1 e 5')

n = random.randint(1, 5)

n1 = int(input('Insira um número de 1 a 5 e tente acertar o numero gerado pelo computador: '))

if n == n1:
    print('Parabéns você acerto!')
else:
    print('Sorry tente mais tarde!')



