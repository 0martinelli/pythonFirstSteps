#ler salario, e calcular aumento

sal = float(input('Insira o valor do seu salário R$ '))

if sal > 1250.00:

    plus = (sal*10)/100

    print('Seu salário com 10% de aumento é: R$ {:.2f}'.format(sal+plus))


elif sal <= 1250.00:

    plus = (sal*15)/100

    print('Seu salário com 15% de aumento é: R$ {:.2f}'.format(sal+plus))


