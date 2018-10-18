#programa de cadastro de pessoas
#ler
#Idade
#Sexo
#perguntar se quer cadastrar mais alguma pessoa
#ao final mostrar:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres de menos de 20 anos

homem = mulher = demaior = menorde20 = 0

escolha = 'S'

while True:

    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite M para Masculino e F para feminino: ')).upper().strip()

    if sexo == 'M':

        homem += 1

        if idade >= 18:

            demaior += 1

    if sexo == 'F':

        mulher += 1

        if idade < 20:

            menorde20 += 1

        elif idade >= 18:

            demaior += 1
    escolha = str(input('Você deseja continuar S ou N? '))

    if escolha in 'Nn':
        break

total = mulher + homem

print(f'Maiores de 18 {demaior}')
print(f'Mulheres com menos de 20 {menorde20}')
print(f'Total de homens cadastrados {homem}')
print(f'Total de pessoas cadastradas: {total}')