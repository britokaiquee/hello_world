# "for" é um loop finito que itera sobre uma sequência específica de elementos.

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    if repeticoes > 2:
        print('\nTentativas excedidas')
        # print('\nVocê excedeu o limite de tentativas')
        break
    repeticoes += 1
    senha_digitada = input(f'Digite a sua senha (tentativa {repeticoes}): ')
    # if senha_salva == senha_digitada:
    #     print('\nVocê entrou')
if senha_salva == senha_digitada:
    print('\nVocê entrou')
# else:
#     print('\nVocê entrou')

# As instruções comentadas acima são alternativas em que todas funcionam, e o
# else seria do bloco while.

print(f'Total de tentativas: {repeticoes}.')
print('\nAquele laço acima pode ter repetições infinitas\n')



# Usando "for":

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')



# "for" por baixo dos panos:

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = 'Kaique'.__iter__() # método dunder iter
# print(texto.__next__()) # metódo dunder next (1º caractere no terminal "K")
# print(texto.__next__()) # 2° (letra "a"), e assim por diante até não ter mais
# ...                     # e estourar o erro "StopInteration"


texto = 'Kaique'  # iterável
# função iter sem precisar escrever o método manualmente
iteratador = iter(texto)  # iterador

while True:
    try:
# função next sem precisar escrever o método manualmente
        letra = next(iteratador) # função next
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)



# O que é usado com "while" também funciona
# com o "for" (break, continue, else, etc)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')