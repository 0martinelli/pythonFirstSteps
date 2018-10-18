#ler varios número inteiros, mostar a soma e o número de números lidos

n1 =0
c = 0
r =0

while n1 != 999:
    n1 = int(input('Insira um número, se você inserir o número 999 o programa irá fechar: '))
    if n1 != 999:

        r += n1

        c +=1

print('soma: {}'.format(r))
print('total: {}'.format(c))



