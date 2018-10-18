#programa que mostre as vogais em palavras de uma tupla

words = ('sim','nao','teste','artic','monkeys','teddy','pikker')

for palavra in words:
    print('\n',palavra, end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')




