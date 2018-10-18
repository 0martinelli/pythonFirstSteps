#fatorial

n = int(input('Insira um número para saber sua fatorial: '))

r = n

while n > 1:
    n -=1
    r *= n

print(r)
