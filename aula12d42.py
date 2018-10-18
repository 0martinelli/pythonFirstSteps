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
    if a == b and a == c and b == c:
        print('Seu triangulo é Equilátero, ou seja possue os três lados iguais')
    elif a == b or a == c or b == c:
        print('Seu Triangulo é isosceles, ou seja pelo menos dois lados dele são iguais')
    elif a != b and a != c and a and b != c:
        print('Seu triangulo possue os três lados de tamanhos distintos, classificando-o como: Escaleno')
else:
    print('Um triangulo não é possível')