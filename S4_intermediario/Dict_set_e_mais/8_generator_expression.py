import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(generator)  # Saída: <generator object <genexpr> at 0x000002BDF1734F40>

print(sys.getsizeof(lista))  # Saída: tamanho da lista em bytes
print(sys.getsizeof(generator))  # Saída: tamanho do generator em bytes

# for n in generator:
#     print(n)  # Saída: todos números em linhas diferentes de 0 até 999999