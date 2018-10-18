#programa que some todos os numeros impares, multiplos de tres entre 1 e 500
s=0

for c in range(0,500+1, 3):
    if c%2 !=0:
        s +=c
        print(s)
print(s)

