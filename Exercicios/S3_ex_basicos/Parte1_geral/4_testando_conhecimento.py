"""
Exercício 4: Testando conhecimentos

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('\nDiga seu nome: ')
idade = (input('\nDiga sua idade: '))
espaco = (' ')

if nome and idade:
    print(f'\nSeu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é "{nome[::-1]}"')
    if espaco in nome:
        print(f'Seu nome contém espaço')
    else:
        print(f'Seu nome não contém espaço')
    print('Seu nome tem', len(nome), 'letras')
    print(f'A inicial do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"')
else:
    print(f'Ops! Você deixou um ou mais campos vazios.')




# Segunda versão:

while True:
    try:
        nome = input('\nQual é o seu nome? ')
        idade = int(input('\nQuantos anos você tem? '))

        if nome and idade:
            print(f'\nSeu nome é {nome} e você tem {idade} ano(s)')
            print(f'Seu nome invertido é "{nome[::-1]}"')
            if ' ' in nome:
                print(f'Seu nome contém espaço(s)')
            else:
                print(f'Seu nome NÃO contém espaço')
            print('Seu nome tem', len(nome), 'caracteres')
            print(f'A inicial do seu nome é "{nome[0]}"')
            print(f'A última letra do seu nome é "{nome[-1]}"')
            break
        else:
            print(f'Ops! Você deixou campos vazios.')

    except ValueError:
        print('Desculpe, você digitou um caractere inválido.')




# Terceira versão:

while True:
    nome = input('\nDigite seu primeiro nome: ')
    # isalpha verifica se todas os caracteres do nome são letras
    if nome.isalpha():
        break
    else:
        print('Por favor, insira apenas letras para o nome.')

while True:
    idade = input('\nDigite sua idade em anos: ')
    # isdigit verifica se todos os caracteres da idade são números
    if idade.isdigit():
        idade = int(idade)  # Converte a idade para inteiro
        break
    else:
        print('Desculpe, você digitou uma idade inválida.')

if nome and idade:
    print(f'\nSeu nome é {nome} e sua idade em anos é {idade}')
    print(f'Seu nome invertido é "{nome[::-1]}"')
    if ' ' in nome:
        print(f'Seu nome contém espaço(s)')
    else:
        print(f'Seu nome NÃO contém espaço')
        print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"\n')
else:
    print(f'Ops! Você deixou campos vazios.')




# Versão do professor:

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
