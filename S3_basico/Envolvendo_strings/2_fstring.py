''' Uma introdução ás f-strings (formatação de strings) '''

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

# É o tipo de formatação preferido do professor, e a mais recém lançada.

print('-'*70)


# Exemplos que o professor não deu:

# Exemplo básico de f-string
nome1 = "Kaique"
idade = 25
altura = 1.75

'''
A barra invertida sozinha "\" indica a continuação do código na próxima linha.
Por ser um escape, ele não é exibido, a menos que use "r", e ele fica roxo numa
string pra diferenciar (quando não é uma str literal ou não tá acompanhado de
outro caractere de escape/aspa).
'''
formato1 = f"Meu nome é {nome1}, tenho {idade} anos e \
minha altura é {altura} metros."
print(formato1)

# F-string com expressões
a = 10
b = 5

formato2 = f"A soma de {a} e {b} é {a + b}."
print(formato2)

# F-string com formatação numérica
pi = 3.14159265359

formato3 = f"O valor de pi com duas casas decimais é {pi:.2f}."
print(formato3)

# Reduzindo a duas casas decimais e separando os milhares com vírgula
valor = 1000052.8
dinheiro = (f'R${valor:,.2f}')
print('Saldo na conta:', dinheiro)

# F-string com operações e alinhamento
nome2 = "Kaique"
sobrenome = "Brito"

formato4 = f"Meu nome completo é {nome2} {sobrenome}."
print(formato4)

# Teste com upper e lower
formato5 = f"Meu nome completo é {nome2.upper():^10} {sobrenome.lower():>10}."
print(formato5)

# upper deixa a str com todos os caracteres em letras maiúsculas e
# lower deixa em letras minúsculas

# F-string com chamada de função
def saudacao(nome3):
    return f"Olá, {nome3}!"

nome3 = "Kaique"
formato6 = saudacao(nome3)
print(formato6)