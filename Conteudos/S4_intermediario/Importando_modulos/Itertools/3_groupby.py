# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

letras = ['a', 'a', 'a', 'b', 'c', 'a']
grupos_de_letras = groupby(sorted(letras))
for chave, grupo in grupos_de_letras:
    print(chave)
    print(list(grupo))

print()


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos_de_alunos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos_de_alunos:
    print(chave)
    for aluno in grupo:
        print(aluno)