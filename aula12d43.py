#calculo de IMC

peso = float(input('Favor, insira seu peso: '))
altura = float(input('Favor, insira sua altura: '))

imc = peso/(altura*altura)

if imc <= 18.5:
    print('Você está abaixo do peso, seu IMC é de {:.2f}'.format(imc))
elif 18.5 < imc <= 25:
    print('Você está no peso ideal seu IMC é de {:.2f}'.format(imc))
elif 25 > imc <= 30:
    print('Você está com sobrepeso, seu IMC é de'.format(imc))
elif 30 > imc <= 40:
    print('Você está obeso, seu IMC é de {:.2f}'.format(imc))
elif imc > 40:
    print('Você está com obesidade mórbida, seu IMC é de {:.2f}'.format(imc))
