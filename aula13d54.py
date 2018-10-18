#programa que le a idade de sete pessoas e mostra quantas delas já são maiores

maior = 0
menor = 0

for c in range(1,8):

    idade = int(input('Digite a idade da pessoa {}: '.format(c)))

    if idade >= 18:
        maior += 1
    else:
         menor += 1

print('O número de pessoas de maior idade é {} e o de menor idade é {}'.format(maior,menor))