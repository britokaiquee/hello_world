'''
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'feminino babylook', 'unisex'],
    ['algodão', 'poliéster']
]

print('Combinações SEM repetições:')
print_iter(combinations(pessoas, 2))

print('Combinações COM repetições:')
print_iter(permutations(pessoas, 2))

print('Produto cartesiano:')
print_iter(product(*camisetas))