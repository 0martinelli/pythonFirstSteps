# identificar se um número é primo

d=0
n1 = int(input('Escreva um número para saber se ele é primo: '))

if n1 == 2:
    print('seu número é primo')

for c in range(2, n1):
    if n1 % c == 0 and c != n1:
        d +=1

if d > 0:
    print('Seu número não é primo')
else:
    print('Seu número é primo')
