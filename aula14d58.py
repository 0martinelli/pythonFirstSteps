#programa onde você deve adivinha o numero escolhido pelo computador

import random
import time

print('Aguarde enquanto o computador está pensando em um número entre 0 e 10')
time.sleep(3)
print('Ok número escolhido')

pc = random.randint(0,10)
escolha = 11
contador = 0


while pc != escolha:
    escolha = int(input('Tente adivinhar o número: '))
    contador +=1

print('Você acertou! O número escolhido pelo computador era: {}!\nPorém precisou de {} tentativas para completar o desafio'.format(pc,contador-1))
