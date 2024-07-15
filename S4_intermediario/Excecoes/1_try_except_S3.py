"""
S3 = Seção 3 do curso (básico)
S4 = Seção 4 (intermediário)
Deixei esse arquivo nessa pasta pra ficar tudo junto

Mensagem de erro

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')
# else:
#     print('Isso não é um número')

# Colocar :.0f deixa sem casas decimais, como se fosse um número int, mas
# continuando sendo float

try:
    ...    # Ellipsis
except:
    pass   # Tem a mesma função do ellipsis, de pular código.