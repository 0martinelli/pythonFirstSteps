#listas
lanche = ['Pizza','Picole','Bacon']

#metodo de adicionar elementos em uma lista
lanche.append('Pipoca')

lanche.insert(2,'Cachorro Quente')

print(lanche)

#metodos de apagar um elemento de uma lista
#del lanche[2]

print(lanche)

#lanche.pop(1)

#lanche.remove('Pizza')

print(lanche)

#organizando de listas

lanche.sort()
print(lanche)
#organização em modo reverso
lanche.sort(reverse=True)

print(lanche)
#

num = [2, 5, 6, 7, 9, 12, 13]

num.sort(reverse=True)

print(num)

num.insert(7,0)

print(num)

num.insert(8,2)

print(num)

valores =[]

valores.append(5)
valores.append(9)
valores.append(4)
valores.append(11)
valores.append(12)

for valor in valores:
    print(f'{valor}....',end=' ')

for c, v in enumerate(valores):
    print(f'Na posição {c} se encontra o valor {v}')

for c in range (0,5):
    valores.append(int(input(f'Digite o valor para ocupar a posição {c}: ')))

a = [2,3,4,7]
b = a

b[2] = 11

print(a)
print(b)

b = a[:]

b[1] = 10
print(b)
