#Um programa que leia dois números inteiros e compare-os para descobrir qual é o maior.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior que o segundo')
elif n2 > n1:
    print('O segundo número é maior que o primeiro')
else:
    print('Os dois números são iguais!')