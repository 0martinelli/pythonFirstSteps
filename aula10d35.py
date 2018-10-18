#programa que le tres retas e define se elas poderam ser um triangulo

a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))

if a < b + c:
    i = 1
else: i=0
if b < a + c:
    j =+1
else: j=0
if c < b + a:
    h =+1
else: h =0

if (i + j + h) == 3:
    print('Um triangulo é possível')
else:
    print('Um triangulo não é possível')