#preencher uma tupla com numeros em extenso
#solicitar ao usuario um numero de 0 a 20 e mostrar esse numero em extenso para o usuario

numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    n = int(input('Insira um número de 0 à 20 para que o computador te mostre o correspondete em extenso: '))

    if n < 0 or n > 20:
        print('Número Inválido')

    else:

        print(f'Seu número em extenso é {numeros[n]}')

