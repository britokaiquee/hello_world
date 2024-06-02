"""
Exercício 12: Lista de compras

Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""


# 1ª versão:

import os

lista = []

while True:
    opcao = input(
    '\n[i]nserir\n[r}emover\n[l]istar\n[a]tualizar\n\nSelecione uma opção: ')
    os.system('cls')
    if opcao.lower() == 'i':
        inserir = input('\nDigite o que você quer inserir: ')
        lista.append(inserir)

    elif opcao.lower() == 'r':
        try:
            apagar = int(input('\nEscolha o índice para remover: '))
            if apagar > 0:
                lista.pop(apagar - 1)
            else:
                print('\nÍndice inexistente.')
        except:
            print('\nÍndice inexistente.')

    elif opcao.lower() == 'l':
        print('\nLista de compras:')
        for indice, item in enumerate(lista, start=1):
            print(indice, item, sep='. ') # sep pra separar o índice do item
        if lista == []:
            print('-'*5) # pra indicar que a lista está vazia
    
    elif opcao.lower() == 'a':
        print('\nAtualizando...')
        break

    else:
        print('\nPor favor, digite uma das letras [i, r, l, a]')


'''
(Do jeito atual tá melhor)
Alternativa pro elif de listar:

    elif opcao.lower() == 'l':
        if lista != []: # também dá certo invertendo com o else
            print('\nLista de compras:')
            for indice, item in enumerate(lista, start=1):
                print(indice, item, sep='. ') # sep pra separar o índice do item
        else:
            print('\nA lista está vazia.')
'''


# 2ª versão com lista fixa e outras mudanças no código:

lista = []

while True:
    print('\nLista de compras 2.0:')

    for indice, item in enumerate(lista, start=1):
        print(indice, item, sep='. ')

    if lista == []:
        print('A lista está vazia.')

    opcao = input('\n[i]nserir\n[a}pagar\n[s]air\n\
\nSelecione uma opção: ')

    if opcao.lower() == 'i':
        inserir = input('\nDigite o que você quer inserir: ')
        lista.append(inserir)

    elif opcao.lower() == 'a':
        try:
            apagar = int(input('\nEscolha o índice para remover: '))
            if apagar > 0:
                del lista[apagar - 1]
            else:
                print('\nÍndice inexistente.')
                input("Pressione enter para continuar... ")
        except:
            print('\nÍndice inexistente.')
            input("Pressione enter para continuar... ")

    elif opcao.lower() == 's':
        print('\nVocê saiu.\n')
        break

    else:
        print('\nVocê não digitou nenhuma das opções.')
        input("Pressione enter para continuar... ")

    os.system('cls')


'''
Não colocar nada junto da variavel "apagar" com o del ou o pop apaga o que vem
depois dele; colocar "+" ele soma o índice que você digitou com o que foi
colocado após o + e apaga o que vem após o número do resultado; já quando é "-"
é o inverso, ele subtrai o valor que você digitou e o número do resultado será
o que ele irá apagar, sendo que quando passa do primeiro da lista ele vai pro
final e continua voltando. Nos casos em que usei (tanto com del quanto com pop)
ele apaga o índice digitado mesmo, porque invés dele apagar o seguinte ele
volta um índice.
'''


# Solução do professor:

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
            )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')