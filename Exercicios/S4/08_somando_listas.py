"""
Exercício 26 - Somando listas.

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


# Escrevendo os códigos em inglês agora

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [1, 2, 3, 4]
sum_list = []

for index in range(len(list_2)):
    result = list_1[index] + list_2[index]
    sum_list.append(result)

print(sum_list)


# Usando a função "min" para saber o índice da menor lista

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
list_c = []

smaller_list = min(len(list_a), len(list_b))

for i in range(smaller_list):
    sum_result = list_a[i] + list_b[i]
    list_c.append(sum_result)

print(list_c)



# Soluções do professor:

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


# Solução 1: com range

lista_soma1 = []
for i in range(len(lista_b)):
    lista_soma1.append(lista_a[i] + lista_b[i])
print(lista_soma1)


# Solução 2: com enumerate

lista_soma2 = []
for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])
print(lista_soma2)


# Solução 3: com list comprehension

lista_soma3 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma3)



'''
Uando zip_longest para pegar os valores até o final da maior lista (ou seja,
todos valores que tem) e fillvalue para substituir os valores que faltam na
menor lista por 0, assim mantendo os mesmos valores da lista_a após o último
da lista_b
'''

from itertools import zip_longest

lista_soma4 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma4)