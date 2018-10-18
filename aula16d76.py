#programa que tenha uma tupla unica com nomes de produtos e seus preços na sequencia
# mostrar precos e produtos de forma tabular

produtos = ('Frango', 3.95, 'Cebola', 4.35, 'Tomate', 4.20, 'Caldo', 1.25)


for x in range(0,len(produtos)):
    if x % 2 == 0:
        print(produtos[x],end='..............R$')
    else:
        print(produtos[x])
