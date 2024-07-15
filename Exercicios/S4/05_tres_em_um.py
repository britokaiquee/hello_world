# Exercícios 21 a 23

import copy

from dados import produtos

'''
1. Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
'''

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]


'''
2. Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
'''

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda item: item['nome'],
    reverse=True
)


'''
3. Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda item: item['preco']
)


# Espaço de exibição

print("Produtos originais:")
print(*produtos, sep='\n')
print()

print("Novos produtos com preços aumentados:")
print(*novos_produtos, sep='\n')
print()

print("Produtos ordenados por nome decrescente:")
print(*produtos_ordenados_por_nome, sep='\n')
print()

print("Produtos ordenados por preço crescente:")
print(*produtos_ordenados_por_preco, sep='\n')
print()


# A solução do professor só tem umas pequenas diferenças
# (me inspirei em umas coisas inclusive)