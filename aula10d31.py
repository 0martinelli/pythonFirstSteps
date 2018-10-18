#programa que le a kilometragem de uma viagem com custo de é 0.50 por km até 200, acima disso o preco sera 0.45

print('Vamos calcular o valor da sua viagem por KM:')
print('Até 200km você pagará R$ 0.50 por KM, acima disso o valor será de R$ 0.45')
n1 = float(input('Quantos KM você rodou na sua última viagem: '))

if n1 > 200:
    gasto = n1*0.45
else:
    gasto = n1*0.50

print('Você gastou R${:.2f}'.format(gasto))

