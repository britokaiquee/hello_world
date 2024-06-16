# Exercícios 5 a 7 - aula 54 da sessão
"""
1. Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Versão com try e except

try:
    numero = int(input('\n1. Digite um número: '))
    resultado = numero % 2 == 0

# Aqui não precisa colocar "is True", apenas se quiser especificar, pois
# a variavel resultado já é classificada como bool e é True. Além disso,
# se converter para False colocando "is False", os resultados serão
# invertidos, isso é, números pares serão ditos como ímpares e vice-versa.
    if resultado:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print('\nDigite apenas números inteiros.')


# Versão com isdigit

numero = input('\n1.1 Digite um número: ')
if numero.isdigit():
    numero = int(numero)
    resultado = numero % 2 == 0

    if resultado:
        print(f'O número {numero} é par')
    elif resultado:
        # Alternativa: colocar "is False" ou "is not True" para especificar que
        # é False em elif
        print(f'O número {numero} é ímpar')
else:
    print('\nDigite apenas números inteiros.')


# Soluções do professor

# Primeira versão:

entrada = input('\n1.2 Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('\nVocê não digitou um número inteiro')


# Segunda versão

entrada = input('\n1.3 Digite um número: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('\nVocê não digitou um número inteiro')


"""
2. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


# Versão com try e except:

try:
    hora = int(input('\n2. Que horas são? '))
    dia = 0 <= hora < 12
    tarde = 12 <= hora < 18
    noite = 18 <= hora <= 23
    if dia:
        print('\nBom dia, Kaique!')
    elif tarde:
        print('\nBoa tarde, Kaique!')
    elif noite:
        print('\nBoa noite, Kaique!')
    else:
        print('\nPor favor, digite um número inteiro entre 0 e 23.')
except:
    print('\nPor favor, digite um número inteiro entre 0 e 23.')


# Versão com isdigit (para digitar só números):

nome = input('\n2.1 Qual é seu nome? ')
hora = input('    Que horas são? ')
if hora.isdigit():
    hora = int(hora)
    dia = 0 <= hora < 12
    tarde = 12 <= hora < 18
    noite = 18 <= hora <= 23
    if dia:
        print(f'\nBom dia, {nome}!')
    elif tarde:
        print(f'\nBoa tarde, {nome}!')
    elif noite:
        print(f'\nBoa noite, {nome}!')
    # exceção para o caso de números abaixo de 0 (negativos) ou acima de 23
    else:
        print('\nNão conheço essa hora.')
# exceção para o caso de tipos diferentes (como str e float)
else:
    print('\nPor favor, digite apenas números inteiros.')


# Solução do professor:

entrada = input('\n2.2 Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('\nNão conheço essa hora')
except:
    print('\nPor favor, digite apenas números inteiros')


"""
3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4
letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Minha versão com isalpha (para digitar só letras):

primeiro_nome = input('\n3. Diga seu primeiro nome: ')
if primeiro_nome.isalpha():
    curto = len(primeiro_nome) <= 4
    normal = 5 <= len(primeiro_nome) <= 6
    grande = len(primeiro_nome) > 6
    if curto:
        print('Seu nome é curto')
    elif normal:
        print('Seu nome tem tamanho normal')
    elif grande:
        print('Seu nome é muito grande')
else:
    print('\nPor favor, digite um nome com letras')
    print(
    'Obs: espaço não conta como letra, então digite apenas seu primeiro nome.')


# Solução do professor:

nome = input('\n3.1 Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('\nDigite mais de uma letra')