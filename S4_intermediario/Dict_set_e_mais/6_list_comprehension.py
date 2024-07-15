# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Vídeo no youtube em que ele fala muito mais sobre list comprehension:
# https://youtu.be/1YbTDczvqco

print(list(range(10)))

lista1 = []
for numero in range(10):
    lista1.append(numero)
print(lista1)

lista2 = [
    numero * 2
    for numero in range(10)
]
print(lista2)



# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos1 = [
    # aumento de 5% no preço caso o preço seja acima de 20
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  # ternário
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos1, sep='\n')



# Filtro de dados em List comprehension (filter)

import pprint  # Para imprimir o dicionário de forma legível


def p(v):  # Função para não ter que repetir a linha abaixo toda vez
    # sort_dicts=False para as chaves não serem exibidas em ordem alfabética
    # width para definir a largura máxima da linha
    pprint.pprint(v, sort_dicts=False, width=40)


# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]


p(novos_produtos2)



# List comprehension com mais de um for

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)
