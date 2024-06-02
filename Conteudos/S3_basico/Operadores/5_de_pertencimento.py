# Operadores de pertencimento
# in | not in

# Strings são iteráveis
#  0 1 2 3 4 5
#  K a i q u e
# -6-5-4-3-2-1

# nome = 'Kaique'
# print(nome[0])
# print(nome[-5])
# print('que' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('que' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    