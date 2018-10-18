#crie um programa que identifique se o valor é par ou impar

n = int(input('Insira um número pra saber se ele é par ou impar: '))

n1 = (n%2)

if n1 == 0:
    print('Seu número é par')
else:
    print('Seu número é impar')
