"""
Exercício 8: Iterando strings com while
"""

nome = 'Kaique Brito'  # Iteráveis
tamanho_nome = len(nome)
print('Nome:', nome)
print('Qtd de caracteres:', tamanho_nome, '\n')

indice = 0

while indice < len(nome):
    caractere = '*' + nome[indice]
    print(caractere, end='')
    indice += 1



# Alternativa:

print() # pra separar da 1ª versão (nesse caso pode ser vazio invés de pôr \n)
i = 0
nova_string = '' # acumulação

while i < len(nome):
    nova_string += f'*{nome[i]}'
    i += 1

print(nova_string)



# Solução do professor:

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*' # para o último caractere também ter asterisco
print(novo_nome)