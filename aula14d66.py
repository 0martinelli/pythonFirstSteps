#programa que usa break quando o numero 999 eh digitado
#mostrar também quantos números foram digitados e a soma deles

s = c = 0

while True:

    n = int(input('Digite um número ou digite 999 para sair: '))

    if n == 999:
        break
    s +=n
    c +=1

print(f'Soma {s}')
print(f'Total {c}')
