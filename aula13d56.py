#desenvolva um programa que leia nome, idade e sexo de 4 pessoas e apresente:
#A idade média
#Nome do Homem mais velho
#Quantas mulheres tem menos de 20 anos

total=0
maior=0
nome = []
idade = []
sexo = []
velha = 0

for c in range(0,4):
    nome.insert(c,input('Digite seu nome: '))
    idade.insert(c,int(input('Digite sua idade: ')))
    sexo.insert(c,input('Digite M para masculino e F para feminino: ').upper())

    total += idade[c]

    if sexo[c] == 'M':
        if maior < idade[c]:
            maior = idade[c]
            velho = c
    total+=idade[c]

    if sexo[c] == 'F':
        if idade[c] < 20:
            velha +=1

media = total/4

print('A media total de idade é igual a: {}'.format(media))
print('O homem mais velho é {}'.format(nome[velho]))
print('A quantidade de mulheres menores de 20 é: {}'.format(velha))
