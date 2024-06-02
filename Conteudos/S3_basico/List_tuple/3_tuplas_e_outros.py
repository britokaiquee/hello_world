"""
Tipo tupla - Uma lista imutável
"""

nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)


print("-" * 20)


"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])


print("-" * 20)


# Alternativa:
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)


print("-" * 20)


# Uso de dois for e o \t (tabulação):

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

# O enumerate retorna listas como tuplas.


print("-" * 20)


"""
Lista de listas e seus índices

Também pode colocar:
Listas em tuplas
Tuplas em listas
Tuplas em tuplas
e etc...
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
    # 0       1       2          3
    # ['Luiz', 'João', 'Eduarda', ( 0, 10, 20, 30, 40)],  # 3
    #                             # 0  1   2   3   4
]

print(salas[0][1])
print(salas[1][0])
print(salas[2][2])
# print(salas[3][3][2])


print('-'*40)


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)


'''Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)'''
