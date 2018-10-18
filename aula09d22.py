# Ler o nome de uma pessoa e mostrar:
# O nome do todas Maiusculas
# O nome com todas minusculas
# Contar quantas letras existem no nome
# Quantas Letras tem o primeiro nome

nome = input('Seu nome completo, por favor: ')

print(nome.upper()) #coloca o nome em maisculas
print(nome.lower()) #coloca o nome em minusculas

nome1 = nome.split() #separa as palavras do nome

print('Seu primeiro nome tem {} letras'.format(len(nome1[0])))

nome2 = '-'.join(nome1) #troca espaços por -

espaco = nome2.count('-') #conta o numero de -

n1 = len(nome) #conta o numero de caracteres total do nome incluindo espaços

total = n1 - espaco #diminui o numero de espacos do tamanho total do nome

print ('Número total de letras sem espaco: {}'.format(total))