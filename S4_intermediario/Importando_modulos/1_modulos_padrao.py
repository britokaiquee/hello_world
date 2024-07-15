'''
Módulos padrão do Python (import, from, as e *)

Todos módulos:
https://docs.python.org/3/py-modindex.html


inteiro - import nome_modulo

Vantagens: você tem o namespace do módulo
Desvantagens: nomes grandes

platform é um atributo do módulo sys, na qual exibe uma str que indica o
sistema operacional no qual o Python está sendo executado
'''

# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)


'''
partes - from nome_modulo import objeto1, objeto2

Vantagens: nomes pequenos (partes específicas do módulo)
Desvantagens: Sem o namespace do módulo
'''

# from sys import exit, platform

# print(platform)


'''
alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido

Vantagens: você pode reservar nomes para seu código dando apelido(s) pro módulo
Desvantagens: pode ficar fora do padrão da linguagem
'''

# # Alias 1

# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# # Alias 2

# from sys import exit as ex
# from sys import platform as pf
# # Alternativa: from sys import exit as ex, platform as pf

# print(pf)


'''
má prática - from nome_modulo import *

Vantagens: usar o asterico importa tudo de um módulo (sem o namespace)

Desvantagens: importa tudo de um módulo. Você pode não saber de onde veio, ou
sobrescrever sem saber que era do módulo também, ou seja, acaba deixando o
código obscuro.
'''

# from sys import exit, platform

# print(platform)
# exit()