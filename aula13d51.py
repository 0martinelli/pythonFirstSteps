#programa que leia o primeiro termo e a razao de uma PA e mostre os dez primeiros termos dessa razao

t1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razao de PA: '))

for c in range(0,r*10,r):
    print(t1+c)


