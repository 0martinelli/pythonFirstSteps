#programa que leia um numero e mostre sua tabuada
#se um numero negativo for inserido o programa para

while True:

    n = int(input('Digite um número para saber sua tabuada: '))

    if n < 0:
        break

    c = 0
    r =0

    for c in range(11):
        r = c * n
        print(f'{n} x {c} = {r}')
print('FIM')