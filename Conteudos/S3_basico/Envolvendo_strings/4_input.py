# O input é uma função que permite a interação do usuário com o programa,
# capturando dados inseridos pelo usuário durante a execução. Essa função
# torna a variável uma string.

nome = input('Qual é o seu nome? ')
print(f'Olá {nome}')

idade = input('Qual é a sua idade? ')
print(f'Sua {idade=}')

# numero = float(input('Digite um número: '))
# numero_0 = int(input('Digite outro número: '))
# print(f'A soma dos números é: {numero+numero_0}')

while True:
    try:
        # Não é bom colocar tudo na mesma linha
        numero_1 = int(input('Digite um número: '))
        # Pois assim não terá como fazer correção
        numero_2 = int(input('Digite outro número: '))
        break
    except ValueError:
        print("Utilize apenas números.")

print(f'A soma dos números é: {numero_1+numero_2}')

# Jeito certo para abrir espaço para fazer um código de checagem:

numero_3 = (input('Digite um número: '))
numero_4 = (input('Digite outro número: '))

# (espaço)

int_numero3 = int(numero_3)
int_numero4 = int(numero_4)
print(f'A subtração dos números é: {numero_1-numero_2}')