#Calcula salário com 15% de aumento

salario = float(input('Valor do salário: R$'))

n = (salario*15)/100

total = salario + n

print('O valor do seu salário com 15% de aumento é de: R${:.2f}'.format(total))
