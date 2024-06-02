"""
Exercício 14: Cálculo do segundo dígito e validador de CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


# Protótipo:

multiplicador = 11
resultado = 0

while True:
    try:
        cpf = input(
            'Digite os primeiros dez dígitos do seu CPF (apenas os números): ')

        if len(cpf) != 10:
            print('Por favor, digite apenas dez dígitos númericos.\n')

        else:
            for n in cpf:
                resultado += int(n) * multiplicador
                multiplicador -= 1
            digito2 = resultado * 10 % 11
            digito2 = digito2 if digito2 <= 9 else 0
            print(f'O segundo dos últimos dois dígitos é: {digito2}')
            break

    except ValueError:
        print('Ocorreu um erro. Digite apenas números.\n')



# Junção do cálculo do primeiro dígito com o segundo:

multiplicador = 10
resultado = 0

while True:
    try:
        cpf_9digitos = input(
        '\nDigite os primeiros nove dígitos do seu CPF (apenas os números): ')
        
        if len(cpf_9digitos) == 9:
            for n in cpf_9digitos:
                resultado += int(n) * multiplicador
                multiplicador -= 1
            digito1 = resultado * 10 % 11
            digito1 = digito1 if digito1 <= 9 else 0
            cpf_10digitos = cpf_9digitos + str(digito1)
                
            multiplicador = 11
            resultado = 0

            for n in cpf_10digitos:
                resultado += int(n) * multiplicador
                multiplicador -= 1
            digito2 = resultado * 10 % 11
            digito2 = digito2 if digito2 <= 9 else 0
            print(f'Os dois últimos dígitos são: {digito1}{digito2}')
            break

        else:
            print('Digite apenas os nove números.')

    except ValueError:
        print('Digite apenas nove dígitos númericos.')



# Versão definitiva, podendo colocar o CPF completo e mais outras melhorias:

multiplicador = 10
resultado = 0

while True:
    try:
        cpf = input('Digite seu CPF: ')
        if not cpf:  # se o usuário pressionar enter sem digitar nada
            print('Você não digitou nada.\n')
            continue
        entrada_sequencial = cpf == cpf[0] * len(cpf) and len(cpf) > 1
        if entrada_sequencial:
            print('Você enviou dados sequenciais.\n')
            continue
        if len(cpf) != 11: # pro caso de não ter exatamente 11 números
            print('Digite apenas os onze números.\n')
            continue

        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        nove_digitos = cpf[:9] # os nove primeiros digitados pelo usuário
        ultimos_digitos = cpf[9:] # os dois últimos

        for n in nove_digitos[:9]:
            resultado += int(n) * multiplicador
            multiplicador -= 1
        digito1 = resultado * 10 % 11
        digito1 = digito1 if digito1 <= 9 else 0
        dez_digitos = nove_digitos + str(digito1)
                
        multiplicador = 11
        resultado = 0
        for n in dez_digitos:
            resultado += int(n) * multiplicador
            multiplicador -= 1
        digito2 = resultado * 10 % 11
        digito2 = digito2 if digito2 <= 9 else 0
        resultado_dos_calculos = f'{digito1}{digito2}' # concatenando

        print(f'\nVerificando: {cpf_formatado}')
        if ultimos_digitos == resultado_dos_calculos:
            print('Seu CPF é válido.\n')
        else:
            print('CPF inválido.\n')
        break

    except ValueError: # pro caso de ter caracteres que não são números
        print('Digite apenas os onze números.\n')


'''
Pro caso de querer colocar pra exibir o resultado dos cálculos:
print(f'Pelos cálculos dos primeiros nove digitos, os dois últimos devem ser (b)
{resultado_dos_calculos}.\n')

Troque (b) pela barra invertida, coloquei assim para não dar problema
E coloque essa função print abaixo da que exibe "verificando".
'''


# Solução do professor:

import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
