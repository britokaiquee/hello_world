"""
Interpolação básica de strings
s - string
d | i - int
f - float
x | X - Hexadecimal (0123456789ABCDEF)
"""
nome = 'Kaique'
preco = 1000.95897643
teste = 'teste'
variavel = '%s, o preço é R$%.2f, %s, %s' % (nome, preco, teste, nome)
print(variavel)
# print('O hexadecimal de %i é %X' % (100, 100))
print('O hexadecimal de %i é %08X' % (1500, 1500))
