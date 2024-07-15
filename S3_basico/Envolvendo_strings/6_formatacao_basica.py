# Aula 45 - sessão 3
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
# Preenche os caracteres restantes com espaço a direita
print(f'{variavel: >10}')
# Mesma coisa só que com 0 (pode ser qauqluer caractere(s))
print(f'{variavel:0>10}')
# Preenche com espaço a esquerda 
print(f'{variavel: <10}.')
# Mesmo processo com outro caractere a esquerda
print(f'{variavel:A<10}')
# Preenche e centraliza a str de acordo o número total de caracteres
print(f'{variavel: ^10}.')

# Imprime o valor numérico 1000.4873648123746 formatado como um número de ponto
# flutuante com 1 casa decimal, preenchido com zeros à esquerda, com sinal, e
# com um total de 10 caracteres, incluindo vírgulas para separar os milhares.
print(f'{1000.4873648123746:0=+10,.1f}')

# Imprime a representação hexadecimal do número inteiro 1500.
print(f'O hexadecimal de 1500 é {1500:X}')

# Para aparecer os caracteres adicionais é necessário colocar uma quantidade
# superior a que já tem, no exemplo abaixo seria mais do que 3 por exemplo
# já que resulta em um valor de hexadecimal de três caracteres (5DC)
print(f'O hexadecimal de 1500 é {1500:08X}')

# !r faz aparecer entre aspas
print(f'{variavel!r}')

# Diferentes maneiras de formatar strings:
# f-string, format e interpoliação
# Lembre-se que os comentários se referem a 1ª linha de código abaixo de cada.