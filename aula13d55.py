#programa que le o peso de 5 pessoas e apresenta o maior e menor peso:

maior = 0
menor = 1000

for c in range (1,6):
    peso = float(input('Informe o pesso da pessoa {}: '.format(c)))

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print('Maior peso {:.2f}'.format(maior))
print('Menor peso {:.2f}'.format(menor))
