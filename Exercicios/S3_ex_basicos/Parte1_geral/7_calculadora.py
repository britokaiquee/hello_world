""" Exercício 9: Criando uma calculadora com while """

while True:
    try:
        entrada = input(
            '\nDigite "I" para iniciar a operação ou "P" para parar: ')
        if entrada == 'I' or entrada == 'i':
            num1 = int(input('Digite o primeiro número: '))
            operador = input('Digite o operador: ')
            num2 = int(input('Digite o segundo número: '))
            if operador == '+':
                print(f'A soma dos dois números é {num1+num2}')
            elif operador == '-':
                print(f'A subtração dos dois números é {num1-num2}')
            elif operador == '*':
                print(f'A multiplicação dos dois números é {num1*num2}')
            elif operador == '**':
                print(f'A exponenciação dos dois números é {num1**num2}')
            elif operador == '/':
                print(f'A divisão dos dois números é {num1/num2}')
            elif operador == '//':
                print(f'A divisão inteira dos dois números é {num1//num2}')
            elif operador == '%':
                print(f'O resto da divisão dos dois números é {num1%num2}')
            else:
                print('Erro: operador inválido.')
        elif entrada == 'P' or entrada == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')

    except:
        print('Erro: valor inválido.')



# Versão atualizada com números flutuantes:

while True:
    try:
        entrada = input(
'\nDigite "I" para iniciar a operação ou "P" para parar, e pressione Enter. \n')
        if entrada == 'I' or entrada == 'i':
            print('\nCalculadora 2.0\n')
            num1 = float(input('Primeiro número:\n'))
            num2 = float(input('Segundo número:\n'))
            operador = input('Operador:\n')
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                resultado = num1 / num2
            elif operador == '//':
                resultado = num1 // num2
            elif operador == '**':
                resultado = num1 ** num2
            elif operador == '%':
                resultado = num1 % num2
            else:
                print('Erro: operador inválido.')
                continue

            # Se o resultado é um número inteiro, converta-o para int
            if resultado.is_integer():
                resultado = int(resultado)
            print(f'\nResultado = {resultado}')
        elif entrada == 'P' or entrada == 'p':
            print('\nVocê saiu.')
            break
        else:
            print('Erro: você não digitou nenhuma das opções.')
    except:
        print('Erro: valor inválido.')



# Versão do professor:

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
