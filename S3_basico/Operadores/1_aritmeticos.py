# Operadores aritméticos

soma = 1 + 1
subtraçao = 2 - 2
multiplicacao = 3 * 3
divisao = 3.98 / 2 # float

# corta as casas decimais quando é uma divisão entre números inteiros
# arredondando sempre pra menos
divisao_inteira1 = 3.98 // 2

# dividir por número flutuante, vai resultar em número flutuante
divisao_inteira2 = 5 // 5.5

exponenciacao = 2 ** 10  # potenciação
modulo1 = 50 % 3  # resto da divisão
modulo2 = 25 % 5

print('Soma:', soma)
print('Subtração:', subtraçao)
print('Multiplicação:', multiplicacao)
print('Divisão:', divisao)
print('Divisão inteira 1:', divisao_inteira1)
print('Divisão inteira 2:', divisao_inteira2)
print('Exponenciação:', exponenciacao)
print('Módulo 1:', modulo1)
print('Módulo 2:', modulo2)
print(9 % 6 == 0)
print(18 % 6 == 0)
# pra saber se é um número par, divide por 2, se resultar em true é par
# e se resultar em false é ímpar
print(20 % 2 == 0)
print(25 % 2 == 0) 

concatenacao1 = 'X' + 'Y' + 'Z'
print(concatenacao1)
concatenacao2 = 'Kaique' + ' ' + 'Brito'
print(concatenacao2)
a_quinze_vezes = 'k' * 15
print(a_quinze_vezes)
Kaique_duas_vezes = 'Kaique ' * 2
print(Kaique_duas_vezes)

# Ordem:
# 1. ( )
# 2. **
# 3. * / // %
# 4. + -

conta1 = 1+1**5+5
conta2 = 1+1**(5+5)
conta3 = (1+int(0.5+0.5))**5+5
conta4 = (1+1)**(5+5)
print(conta1, conta2, conta3, conta4)
print(conta1 + conta2 + conta3 + conta4)



# Scripts do professor:

''' Introdução aos operadores aritméticos (matemática) '''

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo1 = 55 % 2  # resto da divisão
print('Módulo', modulo1)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)


''' Concatenação (+) e repetição (*) com operadores aritméticos '''

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)


''' Precedência entre os operadores aritméticos (ordem de prioridade) '''

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
