# Exercício 25 - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper():
    # Determinando o comprimento da menor lista
    lista_menor = len(cidades) if len(cidades) < len(estados) else len(estados)

    nova_lista = []

    # Iterando pelos índices das listas até o comprimento da menor lista
    for i in range(lista_menor):  # Alternativa sem a variável: range(2)

        # Combinando os elementos das listas em tuplas e adicionar à nova lista
        nova_lista.append((cidades[i], estados[i]))
    return nova_lista

print(zipper())




# Soluções do professor:


def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

zipper()
print()
print(list(zip(l1, l2)))
print()
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
