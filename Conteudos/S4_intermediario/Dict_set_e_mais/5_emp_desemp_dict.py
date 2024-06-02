# Empacotamento e desempacotamento de dicionários


# Atribuição múltipla (fora do assunto)
a = b = 5
print(a, b) # Ambas variáveis são atribuidas ao mesmo valor (recebem o 5)


# Empacotando = colocando no dicionário | Desempacotando = tirando

# Exemplo de troca de valores (empacotamento e desempacotamento simultâneos)
a, b = 1, 2
# Desempacota os valores de b e a, e depois empacota nos novos a e b (inverte os
# valores das variáveis)
a, b = b, a
print(a, b) # Saída: 2 1


# Daqui para baixo só há exemplos de desempacotamento

pessoa1 = {
    'nome': 'Kaique',
    'sobrenome': 'Brito',
}



'''
Falando da próxima linha de código abaixo, sem nenhum metódo ele já fica como
key por padrão. E tem que colocar as variáveis entre parênteses (em forma de
tupla) pra especificar que é chave/valor, porque se não fica como se tivesse
mais variáveis do que argumentos, e aí gerará um erro. Além disso, a variável
sem estar como tupla conta como as duas coisas juntas (chave e valor), sendo
exibida em forma de tupla, ou seja, com -> ('',)
'''

# Desempacotando os itens do dicionário pessoa1
# Ao desempacotar, cada item é uma tupla (chave, valor)
(a1, a2), (b1, b2) = pessoa1.items()
print(a1, a2)  # Saída: nome Kaique
print(b1, b2)  # Saída: sobrenome Brito

# Iterando sobre os itens do dicionário
for chave, valor in pessoa1.items():
    print(chave, valor)


print()

pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}


# Mesclando dois dicionários em um novo dicionário
pessoas_completa = {**pessoa2, **dados_pessoa}
print(pessoas_completa)



'''
args e kwargs
args (já vimos)
kwargs - keyword arguments (argumentos nomeados)
'''


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# Exemplos de chamadas da função com argumentos nomeados
mostro_argumentos_nomeados(1, 2, 3, nome='Joana', qlq=123)
print()
mostro_argumentos_nomeados(**pessoas_completa)
print()


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
