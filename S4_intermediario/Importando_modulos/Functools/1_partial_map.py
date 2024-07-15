# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# partial é usado para não precisar fazer closure
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


# map é usado para não precisar fazer list comprehension.
# Convertendo para list para que o iterador map não se esgote
novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print_iter(novos_produtos)


print(novos_produtos)
print()
print(hasattr(novos_produtos, '__iter__'))  # Para saber se é um iterator
print(hasattr(novos_produtos, '__next__'))  # Para saber se tem next
print(isinstance(novos_produtos, GeneratorType))  # Para saber se é um generator
print()



# Sintaxe do map: map(função, iterável, ...)

print(
    list(map(
        lambda x: x * 3,  # função
        [1, 2, 3, 4]      # iterável
    ))
)
