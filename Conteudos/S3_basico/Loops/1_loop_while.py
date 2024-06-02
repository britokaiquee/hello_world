"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')

    if nome == 'sair':
        print('Você saiu')
        break

    # Colocado após o break para não aparecer a mensagem "Seu nome é saiu"
    print(f'Seu nome é {nome}')

print('Acabou')

###

contador = 0

while contador < 10:
# a função print em cima da variável faz contar de 0 a 9, e embaixo de 1 a 10
# ou seja, dá pra mudar a contagem só mudando a função print de lugar,
# invertendo a linha com a variável.
    contador = contador + 1
    print(contador)

print('Acabou')

###

# Alternativas:

# contador = 0

# while contador <= 10:
# # nesse caso, a função print em cima da variável faz contar de 0 a 10, e
# # embaixo de 1 a 11.
#     print(contador)
#     contador = contador + 1

# print('acabou')

###

# testes

# contagem de 1 a 10 de uma forma alternativa
contagem = 1

while contagem <= 10:
    print(contagem)
    contagem = contagem + 1

print('acabou')

# 11 a 20 na mesma linha e com os números separados por vírgulas:
while contagem <= 20:
    # "end=" é um parametro usado para imprimir tudo na mesma linha, e o que for
    # colocado dentro das aspas é o que será exibido entre as impressões
    print(contagem, end=', ')
    contagem = contagem + 1
print('acabou')

while contagem <= 30:
    contagem = contagem + 1
    print('teste', end=' ') # para que haja espaço entre cada "teste"

while contagem <= 40:
    contagem = contagem + 1
    print('a', end='')

'''
Deixar o end com aspas vazias fará que não tenha nada entre as impressões
e colocar um \n dentro o anulará.
Além disso, uma função print após um bloco sempre é exebida uma
linha após a do bloco, ou seja, faz quebra de linha. Por isso que no caso do
último bloco while as funções print foram exibidas na mesma linha. E no caso do
"\n", ele pula uma linha, deixando a mesma vazia (como um espaço parágrafo
vertical)
'''