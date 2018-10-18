#Condicoes
#

nome = input('Qual é o seu nome: ')

if nome == 'Jeferson':
    print('Prazer, Jeferson')
else:
    print('Uma pena seu nome não ser Gustavo')


n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))

m = (n1+n2)/2

if m >= 6.0:
    print('Parabéns sua média é {:.1f}! Você Passou!'.format(m))
else:
    print('Infelizmente sua média é {:.1f}, você terá que estudar mais'.format(m))

