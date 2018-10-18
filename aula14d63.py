#sequencia de fibonacci

c = 3
t1 = 0
t2 = 1

n1 = int(input('Quantos número da sequência de Fibonacci você quer ver?: '))
print(t1)
print(t2)

while c < n1:
    t3 = t1 + t2

    print(t3)

    t1 = t2
    t2 = t3

    c +=1

