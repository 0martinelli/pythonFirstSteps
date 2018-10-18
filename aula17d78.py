#ler 5 valores de uma lista, mostrar o maior o menor e a localização deles

valores = []

for n in range(0,5):
    valores.append(int(input('Digite um número: ')))

for n in range(0,len(valores)):
    if n ==0:
        maior = valores[n]
        menor = valores[n]
        posmaior = n
        posmenor = n
    if valores[n] > maior:
        maior = valores[n]
        posmaior = n
    elif valores[n] < menor:
        menor = valores[n]
        posmenor = n

print(f'Maior valor {maior}')
print(f'Menor valor {menor}')
print(f'Posição Maior {posmaior}')
print(f'Posição Menor {posmenor}')