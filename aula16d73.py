#tupla com os times do campeonato brasileiro, mostrar os:
#5 primeiros
#4 últimos
#Ordem alfabética
#Posição da chapecoense

brasileirao = ('Palmeiras','Flamengo','Internacional',
               'São Paulo','Grêmio','Atlético-MG','Santos','Fluminense',
               'Cruzeiro','Atlético-PR','Corinthians','Bahia','Botafogo','Vitória','América-MG',
               'Vasco','Chapecoense','Ceará','Sport','Paraná')
print('Os Cinco primeiros')
for c in range(0,5):
    print(f'Na Posição {c+1}: {brasileirao[c]}')
print('\n')
print('Os Quatro últimos')
for c in range(-4,0):
    print(f'Na Posiçao {c+21}: {brasileirao[c]}')

print('\n')

ordem = sorted(brasileirao)

print('Times em ordem alfabética:')
for c in range(0,20):
    print(ordem[c])

print('\n')

n = brasileirao.index('Chapecoense')

print(f'Posição do Chapecoense: {n+1}')


