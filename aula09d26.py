#Ler a frase e mostrar, quantas vezes aparece a letra A, em que posiçao ela aparece a primeira vez, e a posição que ela aparece a ultima vez

frase = input('Escreva uma frase aqui: ')

frase1 = frase.lower().strip()

print('Numero de vezes que a letras A aparece na frase: {}'.format(frase1.count('a')))

print('Posição onde se encontra a primeira letra A: {}'.format(frase1.find('a')+1))

print('Posição onde a letra A aparece pela última vez: {}'.format(frase1.rfind('a')+1))



