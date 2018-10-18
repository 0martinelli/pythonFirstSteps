#programa que leia seis números inteiros e mostre a soma apenas daaqueles que forem pares. Se o valor digitado for impar desconsidero

s =0
for c in range(0,6):
    n = int(input('Digite um número par, para fazermos a soma '))
    if n%2==0:
        s += n

print('O resultado da soma dos números pares digitados é: {}'.format(s))

