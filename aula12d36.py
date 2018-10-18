#Programa para aprovar financiamento de uma casa
#Deve ler:
#Valor da Casa
#Salário
#Anos para pagamento

#Valor da prestação não pode exceder 30% do salário mensal do comprador.

print('============================================================================')
print('Bem vindo ao simulador de investimentos JJMARTINELLI')
vcasa = float(input('Por favor insira o valor do imóvel em reais R$ '))
vsalario = float(input('Por favor insira seu salário mensal: R$ '))
vano = int(input('Por favor insira em quantos anos você pretende pagar essa casa: '))
print('============================================================================')

prestacao = vcasa/(vano*12)
aprovado = (vsalario*30)/100

print('O valor da prestacao da sua casa ficará em: R$ {:.2f} '.format(prestacao))
print('Voce pretende pagar a casa em {} anos'.format(vano))
print('============================================================================')
print('Para que seu empréstimo seja aprovado, o valor da sua prestaçao nao pode execer 30% da sua renda mensal')
print('Que corresponde exatamente a: R$ {:.2f}'.format(aprovado))
print('============================================================================')
print('Processando')
print('============================================================================')

if aprovado > prestacao:
    print('Parabéns seu empréstimo foi aprovado')
else:
    print('Sorry try again')

print('============================================================================')



