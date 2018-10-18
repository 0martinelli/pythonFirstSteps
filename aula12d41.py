#ler a idade do atleta e classificar como:
#Mirim até 9
#Infantil até 14
#Junior até 19
#Senior até 20
#Master acima de 20

from datetime import date

nascimento = int(input('Insira o ano do seu nascimento: '))

anoAtual = date.today().year

idade = anoAtual - nascimento

if idade <= 9:
    print('Sua categoria é Mirim: ')
elif idade >= 10 and idade <= 14:
    print('Sua categoria é Infantil')
elif idade >= 15 and idade <= 19:
    print('Sua categoria é Junior')
elif idade == 20:
    print('Sua categoria é Senior')
elif idade > 20:
    print('Sua categoria é Master')