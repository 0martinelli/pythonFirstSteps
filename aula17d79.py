lista = []

for c in range(0,10):
    n = (int(input('Digite um Número: ')))
    if n in lista:
        print('Esse número já está na lista')
    else:
        lista.append(n)
lista.sort()

print(lista)