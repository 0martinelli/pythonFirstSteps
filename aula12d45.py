#Programa deve jogar JOKEMPO com você

from random import randint

print('Vamos jogar JOKEMPO')
print('1 para Pedra')
print('2 para Papel')
print('3 para Tesoura')

p1 = int(input('Escolha: '))
p2 = randint(1,3)

print('Computador escolhe: {}'.format(p2))

if p1 == p2:
    print('Empate')
elif p1 == 1 and p2 == 2:
    print('Computador escolhe Papel')
    print('Papel embrulha Pedra')
    print('Computador Vence')
elif p1 == 1 and p2 == 3:
    print('Computador Escolhe Tesoura')
    print('Pedra quebra Tesoura')
    print('Computador Perde')
elif p1 == 2 and p2 == 1:
    print('Computador escolhe Pedra')
    print('Papel embrulha Pedra')
    print('Computador Perde')
elif p1 == 2 and p2 == 3:
    print('Computador escolhe Tesoura')
    print('Tesoura corta papel')
    print('Computador Vence')
elif p1 == 3 and p2 == 1:
    print('Computador Escolhe Pedra')
    print('Pedra quebra Tesoura')
    print('Computador Vence')
elif p1 ==3 and p2 == 2:
    print('Computador escolhe Papel')
    print('Tesoura corta papel')
    print('Computador Perde')
