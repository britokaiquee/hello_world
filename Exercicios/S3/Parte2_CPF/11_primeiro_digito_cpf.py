"""
Exercício 13: Cálculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# 1ª versão com lista e isdigit

lista = []
contador = 10
soma = 0

while True:
    cpf = input(
        'Digite os primeiros nove dígitos do seu CPF (apenas os números): ')

    if len(cpf) != 9 or not cpf.isdigit:
        print('Por favor, digite apenas nove dígitos númericos.')

    else:
        for n in cpf:
            lista.append(int(n))
        for n in lista:
            n *= contador
            contador -= 1
            soma += n
        multiplicacao = soma * 10
        resto_divisao = multiplicacao % 11
        digito = resto_divisao if resto_divisao <= 9 else 0
        print(f'O primeiro dos últimos dois dígitos é: {digito}\n')
        break



# 2ª versão com try-except e sem lista/isdigit, além de outras melhorias

multiplicador = 10
resultado = 0

while True:
    try:
        cpf = input(
            'Digite os primeiros nove dígitos do seu CPF (apenas os números): ')

        if len(cpf) != 9:
            print('Por favor, digite apenas nove dígitos númericos.\n')

        else:
            for n in cpf:
                resultado += int(n) * multiplicador
                multiplicador -= 1
            digito1 = resultado * 10 % 11
            digito1 = digito1 if digito1 <= 9 else 0
            print(f'O primeiro dos últimos dois dígitos é: {digito1}\n')
            break

    except ValueError:
        print('Ocorreu um erro. Digite apenas números.\n')



'''
A segunda versão possui 18 linhas, mas poderia ser 11 sem o input (contando
com a variavel do número do cpf e da iteração, o que seriam duas linhas), a
exceção, a condicional e o bloco while. Já a primeira versão também 20, mas
poderia ser 13 sem a lista, o input, a condicional e o bloco while.
'''



# Solução do professor

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)