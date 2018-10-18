#Escrever um programa que leia o nome de uma pessoa e apresente o primeiro e ultimo nome.

nome = input('Insira seu nome aqui: ')

nome1 = nome.split()

fim = int(len(nome)) #busca o tamanho total da string digitada

inicio = int(nome.rfind(' ')) #busca o ultimo espaço digitado pelo usuário

print(nome1[0])
print(nome[inicio:fim]) #imprime a posicao do inicio, ou seja do ultimo espaco, ate o fim, ou seja do tamanho total da string

