#programa que le um valor em metros, e mostra o distância correspondente em centimetros e milimetros
n1 = int(input('Insira um valor em metros '))

cm = n1*100
mm = n1*1000

print('Esse valor corresponde a {} centimetros e {} milimetros'.format(cm,mm))
