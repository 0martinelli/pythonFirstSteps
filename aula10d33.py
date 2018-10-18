#programa que le tres numeros e mostra o maior deles

n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))

if n1 > n2:
    c = n1
    #print(c)
else:
    c = n2
    #print(c)

if c < n3:
    c = n3

print('O maior número é: {}'.format(c))

if n1 < n2:
    d = n1
else:
    d = n2

if d > n3:
   d = n3

print('O menor número é: {}'.format(d))

