""" while/else (recurso peculiar do Python)"""

string = 'Valor qualquer'

# a variável "i" é comumente usada pelos programadores para contar o index
i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')