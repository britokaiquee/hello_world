"""
split e join com list e str

split - divide uma string (list)
join - une uma string
strip - tira os espaços do ínicio e do final da string
rstrip - tira os espaços da direita (final)
lstrip - tira os espaços da esquerda (ínicio)
"""

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

# a string antes do join é o separador, e ele só funciona com iteráveis
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)