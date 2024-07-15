"""
Empacotamento e desempacotamento
"""

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

# Underline "_" como variável geralmente é usada para indicar que a variável
# não está sendo usada e é pra ser ignorada


print('-'*50)


"""
Desempacotamento em chamadas de métodos e funções:
"""

lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
print(lista)

# O "*_" nesse caso seria "entre uma parte e outra" invés de resto
# Nesse exemplo ele está pulando os índices 1, 2 e 3 (Helena, 1 e 2
# respectivamente)
primeiro, segundo, *_, penultimo, ultimo = lista
print(primeiro, ultimo, penultimo)


print('-'*50)


for nome in lista:
    print(nome, end=' ')
    # Se tirar o " , end=' ' " os elementos ficam em linhas diferentes

print('(for)\n')

print(*lista)
# Nesse caso está fazendo o mesmo que o bloco "for" com o uso do asterisco "*"
# E basicamente o asterico é para tirar os colchetes e aspas
# Se colocar " , sep='\n' " na frente, os elementos ficam em linhas diferentes

print('\nMaria', 'Helena', 1, 2, 3, 'Eduarda', end=' ')
print('(print normal)')


print('-'*50)


string = 'ABCD'
print(*string)
tupla = 'Python', 'é', 'legal'
print(*tupla)


print('-'*50)


salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(*salas, sep='\n')
print()
