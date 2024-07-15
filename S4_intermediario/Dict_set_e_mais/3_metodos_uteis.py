# Métodos úteis dos dicionários em Python


# Criando um dicionário de exemplo
dicionario = {'a': 1, 'b': 2, 'c': 3}

# len - quantas chaves
print("\nQuantidade de chaves:", len(dicionario))
# Saída: 3


# keys - iterável com as chaves
print("\nChaves do dicionário:", dicionario.keys())
# Saída: dict_keys(['a', 'b', 'c'])


# values - iterável com os valores
print("\nValores do dicionário:", dicionario.values())
# Saída: dict_values([1, 2, 3])


# items - iterável com chaves e valores
print("\nChave-Valor do dicionário:", dicionario.items())
# Saída: dict_items([('a', 1), ('b', 2), ('c', 3)])


# setdefault - adiciona valor se a chave não existe
dicionario.setdefault('d', 4)
print("\nDicionário após setdefault:", dicionario)
# Saída: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# get - obtém uma chave
print("\nValor para a chave 'a':", dicionario.get('a'))
# Saída: 1


# pop - Apaga um item com a chave especificada (del)
dicionario.pop('a')
print("\nDicionário após pop('a'):", dicionario)
# Saída: {'b': 2, 'c': 3, 'd': 4}


# popitem - Apaga o último item adicionado
dicionario.popitem()
print("\nDicionário após popitem():", dicionario)
# Saída: {'b': 2, 'c': 3}


# update - Atualiza um dicionário com outro
dicionario.update({'c': 30, 'd': 40, 'e': 5})
print("\nDicionário após update:", dicionario)
# Saída: {'b': 2, 'c': 30, 'd': 40, 'e': 5}


# copy - retorna uma cópia rasa (shallow copy)
copia = dicionario.copy()
print("\nCópia rasa do dicionário:", copia)
# Saída: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Exemplo com cópia profunda (deep copy)
import copy

# Criando um dicionário com objetos aninhados
dicionario_original = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}}

# Realizando uma cópia profunda
copia_profunda = copy.deepcopy(dicionario_original)

# Modificando a cópia profunda
copia_profunda['a'][0] = 100
copia_profunda['b']['x'] = 1000

# Exibindo os dicionários original e a cópia profunda
print("\nDicionário Original:", dicionario_original)
print("Cópia Profunda:", copia_profunda)




print('\n\nProfessor:')
# Exemplos do professor

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

# semelhante ao get, só que com valor invés de chave
pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# faz a mesma coisa que o enumerate
# for chave, valor in pessoa.items():
#     print(chave, valor)

# import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = copy.copy(d1)
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)