#programa que mostra o numero anterior e o proximo de uma entrada digitada
num1 = int(input('Digite um número: '))

before = num1 - 1
after = num1 + 1

print('O número digitado é {}, seu antecessor é o número {} e seu predecessor é o número {}'.format(num1,before,after))