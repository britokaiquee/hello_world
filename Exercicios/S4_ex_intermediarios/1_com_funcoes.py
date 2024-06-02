# Exercícios 16 a 17: Usando funções

'''
1. Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
'''


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


numeros = 1, 2, 3, 4, 5
resultado = multiplicacao(*numeros)
# alternativa sem a variável números (diretamente):
# resultado = multiplicacao(1, 2, 3, 4, 5)
print(resultado)


# Solução do professor:

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)



'''
2. Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
'''


# Primeira versão
def par_impar(numero):
    if numero % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')


par_impar(5)


# Segunda versão com *args
def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f'{numero} é um número par.')
        else:
            print(f'{numero} é um número ímpar.')


numeros = 5, 7, 10, 2, 3, 0, 1
par_impar(*numeros)


# Terceira versão com return e tirando as funções print
def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é um número par.'
    return f'{numero} é um número ímpar.'


while True:
    try:
        entrada = int(
            input('\nDigite um número ou qualquer coisa pra sair: '))
        print(par_impar(entrada))
        # break
    except:
        break
        # print('Digite apenas números inteiros.\n')


# Solução do professor:

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)
