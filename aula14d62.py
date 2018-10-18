#PA perguntando a PA ao usuário

n1 = int(input('Insira aqui o primeiro termo da PA: '))
n2 = int(input('Insira aqui a razão da PA: '))
n3 = int(input('Insira aqui o número de termos que você deseja ver dessa PA: '))

c = 0

if n3 == 0:
    print('Número de termos inválido')

else:
    while c < n3:

        print(n1)
        n1 += n2
        c += 1