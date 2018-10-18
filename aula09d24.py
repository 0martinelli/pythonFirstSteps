# testar se o nome da cidade digitado comeca com a palavra santo

c = input('Digite o nome da cidade: ')

up = c.upper()

n1 = up.split()

print(n1[0].find('SANTO'))
