# Dictionary Comprehension e Set Comprehension

# Tem comprehension pra list, dict e set.
# Só não pra tuple que em vez disso é Generator Expression (expressão geradora).

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc1 = {
    # Assim é melhor, poois a alternativa abaixo deixa margem pra erro
    chave: valor.upper()
    if isinstance(valor, str) else valor
    # Alternativa: chave: valor
    # if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    # == para aparecer só essa chave | =! para não aparecer a chave
    if chave != 'categoria'
}

print(dc1)
print()


lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc2 = {
    chave: valor
    for chave, valor in lista
}

print(dict(lista))
print()


s1 = {i for i in range(10)}
print(s1)

print(set(range(10)))

s2 = {2 ** i for i in range(10)}
print(s2)
