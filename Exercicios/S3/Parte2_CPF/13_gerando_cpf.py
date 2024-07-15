# Exercício 15: Gerador de CPF

# Minha versão:

import random

while True:
    resposta = input(
        '\nDigite "sim" para gerar um CPF\nOu qualquer coisa caso não -> ')
    if resposta.lower() == 'sim': # Converte letras maiúsculas em minúsculas
        try:
            quantidade = int(input('\nQuantos CPFs você deseja gerar? '))

            # Gerando os primeiros nove dígitos e pondo um limite de quantidade
            if quantidade <= 100:
                for _ in range(quantidade):
                    nove_digitos = ''
                    for i in range(9):
                        # Gera nove números de 0 a 9
                        nove_digitos += str(random.randint(0, 9))

                    # Cálculo do primeiro dígito
                    multiplicador = 10
                    resultado = 0
                    for n in nove_digitos[:9]:
                        resultado += int(n) * multiplicador
                        multiplicador -= 1
                    digito1 = resultado * 10 % 11
                    digito1 = digito1 if digito1 <= 9 else 0
                    dez_digitos = nove_digitos + str(digito1)

                    # Cálculo do segundo dígito
                    multiplicador = 11
                    resultado = 0
                    for n in dez_digitos:
                        resultado += int(n) * multiplicador
                        multiplicador -= 1
                    digito2 = resultado * 10 % 11
                    digito2 = digito2 if digito2 <= 9 else 0

                    # CPF gerado pelo cálculo
                    cpf = f'{nove_digitos}{digito1}{digito2}'

                    # Formatando com os pontos e o traço
                    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
                    print(f'{cpf_formatado}')
            else:
                print('O limite é 100 por vez.')

        except ValueError:
                print('Digite apenas números para a quantidade.')
                continue
    else:
        print('\nVocê saiu.')
        break



# Versão do professor:

# import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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

    print(cpf_gerado_pelo_calculo)
