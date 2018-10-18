#programa que tenha menus para executar operancao de dois numeros inseridos pelo usuario

v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))
maior = 0
c = 0

while c != 5:
    print('Escolha a opção abaixo')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Número maior')
    print('[4] Novos números')
    print('[5] Sair')
    c = int(input('Escolha: '))

    if c == 1:
        print('A soma dos números é: {}'.format(v1+v2))

    if c == 2:
        print('O produto dos números é: {}'.format(v1*v2))

    if c == 3:
        if v1 > v2:
            maior == v1
            print('O Maior número é: {}'.format(v1))
        else:
            print('O maior número é: {}'.format(v2))

    if c == 4:
        v1 = int(input('Insira o novo número na posição 1: '))
        v2 = int(input('Insira o novo número na posição 2: '))

print('Obrigado por usar o programa')