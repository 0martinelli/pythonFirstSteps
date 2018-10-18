#Programa que le um número em decimal e entao deixa o usuario escolher se o numero sera impresso em:
#binario
#octal
#hexadecimal

n1 = int(input('Insira um número decimal qualquer: '))
choise = int(input('Digite 1 para converter para Binario, 2 para Octal e 3 para Hexadecimal: '))

if choise == 1:
    print('Seu número em binário: {}'.format(bin(n1)))
elif choise == 2:
    print('Seu número em octal: {}'.format(oct(n1)))
elif choise == 3:
    print('Seu número em hexadecimal: {}'.format(hex(n1)))
else:
    print('Sorry, opção inválida')
