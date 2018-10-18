#Leia um número e apresente seu numero redondo

from math import floor

n = float(input('Digite um numero com duas após a virgula: '))

print('O número inteiro correspondente ao número digitado é: {}'.format(floor(n)))