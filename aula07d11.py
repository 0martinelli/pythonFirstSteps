# programa que calcula a quantidade de tinta a ser usada para pintar uma parede

base = float(input('Insira por favor a largura em metros: '))
altura = float(input('Insira por favor a altura em metros: '))

area = base * altura

litros = area / 2

print('Área total da parede a ser pintada {} metros quadrados'.format(area))
print('Litros te tinta necessários {:.2f}'.format(litros))
