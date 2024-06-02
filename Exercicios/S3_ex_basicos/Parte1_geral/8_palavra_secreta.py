"""
Exercício 10: Jogo da palavra secreta (Forca)

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# 1ª tentativa / versão sem o ajuste da ordem das letras

palavra = 'python'
tamanho = len(palavra) # dá para usar o len diretamente
palavra_secreta = '' # ou formatada
tentativas = 0

while True:
    if palavra_secreta != palavra:
        letra = input('\nDigite uma letra: ')
        if len(letra) == 1:
            if letra in palavra and letra not in palavra_secreta:
                palavra_secreta += letra
        else:
            print('Digite apenas uma letra.')
        print(f'\n{palavra_secreta:-<{tamanho}}')
        tentativas += 1 # concatenando
    else:
        print('\nPARABÉNS, VOCÊ GANHOU!')
        print(f'Total de tentativas: {tentativas}\n')
        break


# 2ª versão:

palavra = 'laranja'
tamanho = len(palavra)
# Alternativas: colocar "_" ou "-" no lugar de "*"
palavra_secreta = '*' * tamanho
tentativas = 0

while palavra_secreta != palavra:
    letra = input('\nDigite uma letra: ')
    if len(letra) == 1: 
        if letra in palavra:
            for i in range(tamanho):
                if palavra[i] == letra:
                    palavra_secreta = palavra_secreta[:i] + letra + \
                        palavra_secreta[i+1:]
            print(palavra_secreta)
        else:
            print(palavra_secreta)
    else:
        print('Digite apenas uma letra.')

    tentativas += 1

print('\nPARABÉNS, VOCÊ GANHOU!!')
print(f'Total de tentativas: {tentativas}\n')


# 3ª e última versão:

import os

palavra_secreta = 'kaique'
tamanho = len(palavra_secreta)
letras_acertadas = '_' * tamanho
tentativas = 0

print('\n\tJOGO DA PALAVRA SECRETA')
while True:
    if letras_acertadas == palavra_secreta:
        os.system('cls')
        print('\n\tPARABÉNS, VOCÊ GANHOU!')
        print(f'\tTotal de tentativas: {tentativas}\n')
        letras_acertadas = '*' * tamanho
        tentativas = 0
        continue

# para que o usuário possa digitar tanto letras minúsculas quanto maiúsculas
# O lower converte maiúsculas em minúsculas
    letra = input('\nDigite uma letra: ').lower()
    if len(letra) == 1: # alternativa: "< 2"
        if letra in palavra_secreta and letra not in letras_acertadas:
            for i in range(tamanho):
                if palavra_secreta[i] == letra:
                    letras_acertadas = letras_acertadas[:i] + letra + \
                        letras_acertadas[i+1:]
    else:
        print('Digite apenas uma letra.')

    print(f'\n{letras_acertadas}')
    tentativas += 1



# Solução do professor
# Obs: comente os códigos de cima pra que esse seja exibido

import os # os = operational system = sistema operacional

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('\nDigite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
# Lógica: a palavra formada é composta por letras secretas que são da palavra
# secreta e veio das letras acertadas que veio das letras digitadas pelo usuário

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls') # Para limpar o terminal e exibir a mensagem final
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
