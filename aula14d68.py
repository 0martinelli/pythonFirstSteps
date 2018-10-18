#programa que joga par ou impar com o usuario vs o computador

import random
import time

vitorias = 0

while True:

    print('Vamos Jogar Par ou Impar com o computador')
    parimpar = int(input('Digite 1 para impar 2 para par: '))

    escolha = int(input('Digite um número de 1 a 3 para jogar: '))

    print('Computador está fazendo a escolha dele')
    escolhapc = random.randint(1,3)
    time.sleep(2)

    print(f'Computador escolheu {escolhapc}')

    soma = escolha + escolhapc

    print(f'Soma das jogadas é: {soma}')

    if soma % 2 == 0 and parimpar == 1:
        print('Você Ganhou!')
        vitorias += 1

    elif soma % 2 == 0 and parimpar == 2:
        print('Você Perdeu!')
        break
    elif soma % 2 != 0 and parimpar == 2:
        print('Você Ganhou!')
        vitorias += 1
    elif soma % 2 !=0 and parimpar == 1:
        print('Você Perdeu')
        break

print(f'Vitórias consecutivas {vitorias}')