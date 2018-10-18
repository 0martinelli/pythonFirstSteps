#calcular  média de um aluno <5 reprovado entre 5 e 6.9 recuperacao acima de 7 aprovado

n1 = float(input('Favor insira sua primeira nota: '))
n2 = float(input('Favor insira sua segunda nota: '))

m = (n1 + n2)/2

print('Sua média é: {:.1f}'.format(m))
if m <= 5:
    print('Você foi reprovado')
elif m > 5 and m < 6.9:
    print('Voce esta em recuperacao')
else:
    print('Voce foi aprovado')