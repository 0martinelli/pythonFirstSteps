#programa para calcular condições de pagamento.

print('Vamos ajustar a forma de pagamento do seu produto')
valor = float(input('Digite o valor da sua compra: R$ '))
print('Digite 1 para pagar a vista Dinheiro/Cheque e ganhe 10% de desconto')
print('Digite 2 para pagar a vista no cartão de debito e ganhe 5% de desconto')
print('Digite 3 para pagar em até 2x no cartão e pague o preço normal')
print('Digite 4 para pagar em 2x ou mais e pague 20% de juros no cartão de crédito')
op = int(input('Digite a opção: '))

if op ==1:

    desconto = (valor*10)/100

    print('O preço final do seu produto será: R${:.2f}'.format(valor-desconto))

elif op==2:

    desconto = (valor*5)/100
    print('O preço final do seu produto será: R${:.2f}'.format(valor-desconto))

elif op==3:

    print('O valor final do seu produto será o valor inteiro: R${:.2f}'.format(valor))

elif op==4:

    acrescimo = (valor*20)/100

    print('O valor final do seu produto será: R$ {:.2f}'.format(acrescimo+valor))
