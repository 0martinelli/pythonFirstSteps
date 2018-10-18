#programa para ler lista de super mercado
#ler nome e valor
#retornar o valor total
#retornar quantos produtos custam mais que R$ 1000,00
#retornar o nome do produto mais barato

total = maisdemil = barato = c = 0

while True:

    c +=1

    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$'))

    total += valor

    if valor > 1000:
        maisdemil +=1

    if c == 1:
        barato = valor

    if valor < barato:
         barato = valor
         nomebarato = nome
    escolha = int(input('Digite 1 para novo produto 2 para finalizar e ver os dados'))

    if escolha == 2:
        break

print(f'Valor total da compra R${total}')
print(f'Quantidade de produtos que custaram mais de Mil Reais: {maisdemil}')
print(f'Nome do produto mais barato {nomebarato}')

