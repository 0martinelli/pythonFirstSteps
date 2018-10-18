#ler quatro valores, guardar em uma tupla e mostrar quantas vezes o valor 9 apareceu, em que posição apareceu o numero 3, quais foram os números pares

num = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))

print(f'Quantidade de números 9: {num.count(9)}')
print(f'Posição do número 3: {num.index(3)+1}')

for x in num:

    if x %2 ==0:
        print(f'Números pares: {x}')