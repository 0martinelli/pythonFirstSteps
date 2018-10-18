#sorteio de alunos

from random import choice

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

a5 = choice([a1, a2, a3, a4])

print('Aluno escolhido {}'.format(a5))