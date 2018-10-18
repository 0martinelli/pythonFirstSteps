
num1 = input('Digite um número: ')
num2 = input('Digite mais um numero: ')
soma = int(num1) + int(num2)
#print('A soma entre ',num1,'e ', num2, 'Vale ', soma) #Sintax antiga
print('A soma entre {} e {} vale {}'.format(num1,num2,soma)) #Sintax Nova

#Teste de tipo

num3 = input('Digite algo')
print(num3.isnumeric()) #Checka se o valor digitado pode ser convertido para um tipo numérico

alf = input('Digite algo ')
print(alf.isalpha()) #teste de tipo para alfanumérico

teste = input('Digite algo')
print('é Alfanumerico?')
print(teste.isalpha())
print('É numérico?')
print(teste.isnumeric())
print('É Decimal?')
print(teste.isdecimal())
print('É digito?')
print(teste.isdigit())
print('É lower case?')
print(teste.islower())
print('É Upper Case?')
print(teste.isupper())

