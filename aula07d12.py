#Programa que dá 5% de desconto em qualquer produto

preco = float(input('Insira o valor do produto:R$ '))

porcento = (preco*5)/100

total = preco - porcento

print('O valor total com desconto de 5% é de: R${:.2f}'.format(total))

