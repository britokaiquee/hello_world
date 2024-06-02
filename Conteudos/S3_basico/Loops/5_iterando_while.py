# Iterando strings com while

frase = 'O Python é uma linguagem de programação' \
'multiparadigma.' \
'Python foi criado por Guido Van Rossum.'

'''
barra invertida "\" é usado como quebra de linha para strings no código, mas
sempre tem que haver aspas entre as partes da string em casa linha. Não sendo
necessário dentro de função print, pois você pode expandi os parentêses de
modo que tenham mais linhas.
'''

# Teste aleatório
# i = 0
# nova_frase = ''
# while i < len(frase):
#     nova_frase += frase[i]
#     # print(nova_frase) # aqui dentro faz aumentar de uma em uma letra
#     i += 1
# print(nova_frase)


# Para saber quantas vezes cada caractere apareceu:

i = 0
while i < len(frase):
    letra_atual = frase[i]
    qtd_letras = frase.count(letra_atual)
    i += 1
    # Não contar os espaços
    if letra_atual == ' ':
        # Se deixar sem esse print, fica a frase toda sem espaços
        print('')
        continue
    print(f'{letra_atual}|{qtd_letras}')


# Para saber qual foi a letra que apareceu mais vezes na frase:

i = 0
qtd_mais = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    # Não contar os espaços
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_mais < qtd_atual:
        qtd_mais = qtd_atual
        letra_mais = letra_atual

    i += 1

print(
    '\nA letra que apareceu mais vezes foi '
    f'"{letra_mais}" que apareceu '
    f'{qtd_mais}x'
)

# Obs: caso haja empates, a letra que apareceu primeiro na frase que será
# exibida no terminal. Como é o caso do "o", já que "a" também apareceu 9 vezes.
# E se colocar menor ou igual invés de só menor "if qtd_mais <+ qtd_atual:", a
# última letra que será exibida invés da primeira.