#programa que leia a idade de um rapaz e tenha como retorno o resultado de alistamento ou nao

from datetime import date

nascimento = int(input('Informe o seu ano de nascimento por favor: '))

ano = date.today().year

idade = ano - nascimento

if idade > 18:
    (print('Você já passou do prazo de alistamento, e deveria ter feito isso a {} anos'.format(idade - 18)))
elif idade < 18:
    (print('Você ainda está apto para se alistar e deverá fazer isso nos proximos {} anos'.format(18 - idade)))
elif idade == 18:
    print('Você deve se alistar este ano!')
