# funcao para sortear grupos e mostrar a ordem

from random import shuffle

a1 = input('Grupo 1: ')
a2 = input('Grupo 2: ')
a3 = input('Grupo 3: ')
a4 = input('Grupo 4: ')

grupos =[a1, a2, a3, a4,] #importante sempre colocar entre conchetes pq isso denota lista

shuffle(grupos)

print('Ordem de apresentaçao dos grupos é: {}'.format(grupos))
