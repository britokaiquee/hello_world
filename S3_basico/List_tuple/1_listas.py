"""
Listas em Python (após o arquivo " 5_constante.py ")
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2               3    4
#       -5   -4     -3              -2   -1
lista = [123, True, 'Kaique Brito',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))


print("-" * 50) # Para separar por partes


#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
# aqui essa variavel abaixo estaria sobrescrevendo a anterior, não sendo
# possivel aparecer os dois valores juntos no terminal
# ultimo_valor = lista.pop(4)
print(lista, 'Removido,', ultimo_valor)

lista.append('Kaique')
nome = lista.pop()
print(nome)  # O pop remove o último elemento da lista e o guarda na memória
lista.append(123)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])


print("-" * 50)


lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_c = lista_1 + lista_2
lista_1.extend(lista_2)
print(lista_1)


lista_1 = ['Luiz', 'Maria', 1, True, 1.2]
# deixar sem o copy faz a lista 1 e 2 serem a mesma lista, isso é, se você
# alterar uma, a outra também alterará. Agora com o copy serão duas listas
# iguais só que separadas, sem precisar reescrever tudo no caso da lista 2
lista_2 = lista_1.copy()

lista_1[0] = 'Qualquer coisa'
print(lista_1)
print(lista_2)


print("-" * 50) 


"""
Listas são iteráveis
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))


print("-" * 50)