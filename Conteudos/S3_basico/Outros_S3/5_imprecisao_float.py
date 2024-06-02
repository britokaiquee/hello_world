"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754

Sobre a imprecisão:
https://en.wikipedia.org/wiki/Double-precision_floating-point_format

Documentação Python do Python:
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

# Usando float padrão do Python

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2  # soma imprecisa de dois floats
print(numero_3)  # imprime o resultado da soma

# " :.2f " é um especificador de formato que exibe o número com duas casas
# decimais, mas sem arredondar. Ele retorna uma str em vez de int ou float, e se
# não fosse str, retornaria float mesmo que todas casas decimais sejam cortadas.
print(f'{numero_3:.2f}')

# round exibe o número arredondado para uma casa decimal. Se você omitir a
# quantidade de casas decimais ou passar 0, ele arredonda para um inteiro (int)
print(round(numero_3, 1))


print('-'*10)


# Usando Decimal ("D" maiúsculo) do módulo decimal ("d" minúsculo)

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
# soma imprecisa de dois Decimals com precisão padrão
numero_3 = numero_1 + numero_2
print(numero_3)


print('-'*10)


# Usando com strings para precisão exata

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
# soma precisa de dois Decimals com precisão definida pelas strings
numero_3 = numero_1 + numero_2
print(numero_3)