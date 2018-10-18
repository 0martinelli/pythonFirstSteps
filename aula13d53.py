#ler uma frase e dizer se ela é um palindromo

frase = str(input('Escreva sua frase pra testarmos a situaçao de palindromo: ')).strip().lower().replace(" ", "")

reversa = frase[::-1]

if frase == reversa:
    print('Sua frase é um Palindromo')

