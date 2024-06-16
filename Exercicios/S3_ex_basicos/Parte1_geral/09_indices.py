"""
Exercício 11: Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
nomes = ['Maria', 'Kaique', 'Luiz']

for i in range(len(nomes)):
    print(i, nomes[i])

####

print("-" * 25)

# Versão do professor

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
