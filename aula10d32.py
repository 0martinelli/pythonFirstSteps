#Programa que calcula se um ano é bisexto

ano = int(input('Digite um ano para que seja feito o calculo se o mesmo é bisexto: '))

rd = ano%4

if rd == 0:
    rd1 = ano%100
    if rd1 != 0:
        print('Seu ano é bisexto!')
    else:
        print('Seu ano não é bisexto!')
else:
    print('Seu ano não é bisexto!')

