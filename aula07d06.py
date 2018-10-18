#programa que exibe o dobro, o triplo e a raiz quadrada de uma entrada digitada
num1 = int(input('Insira um valor qualquer: '))

dobro =  num1*2
triplo = num1*3
raiz =  num1**(1/2)

print('O numero digitado é {}, o dobro desse número corresponde a {}, o triplo é {} e a raiz quadrada desse mesmo número é {}'.format(num1, dobro,triplo,raiz))