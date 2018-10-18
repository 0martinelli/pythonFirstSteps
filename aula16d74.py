#gerar cinco números aleatórios, colocalos em uma tupla e dizer qual é o maior e o menor número

import random

numeros = []

numeros.extend(range(0,5))

for c in range(0,4):

    numeros[c] = random.randint(0,15)

    if c == 0:

        maior = numeros[c]
        menor = numeros[c]

    if numeros[c] > maior:
        maior = numeros[c]

    if numeros[c] < menor:
        menor = numeros[c]


print(f'Sua tupla é: {tuple(numeros)}')
print(f'Maior elemento da Tupla {maior}')
print(f'Menor elemento da Tupla {menor}')

