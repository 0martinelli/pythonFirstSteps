#leia a entrada do usuário e escreva a tabuada do número escrito

n = int(input('Escreva um número para saber sua tabuada '))

for c in range(0,11):
    r = n*c
    print('{} x {} = {}'.format(n,c,r))