# Exercício 19 - sistema de perguntas e respostas

# PRIMEIRA VERSÃO

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


acertos = 0

print(f'Questão 1: {perguntas[0]['Pergunta']}')

for opcoes in enumerate(perguntas[0]['Opções']):
    indice, valor = opcoes

    print(f'{chr(97 + indice).upper()}) {valor}')

resposta = input('\nDigite apenas a opção: ')
if resposta.upper() == 'C':
    print('Certa resposta! ✅\n')
    acertos += 1
else:
    print('Errou ❌\n')


print(f'Questão 2: {perguntas[1]['Pergunta']}')

for opcoes in enumerate(perguntas[1]['Opções']):
    indice, valor = opcoes

    print(f'{chr(97 + indice).upper()}) {valor}')

resposta = input('\nDigite apenas a opção: ')
if resposta.upper() == 'A':
    print('Certa resposta! ✅\n')
    acertos += 1
else:
    print('Errou ❌\n')


print(f'Questão 3: {perguntas[2]['Pergunta']}')

for opcoes in enumerate(perguntas[2]['Opções']):
    indice, valor = opcoes

    print(f'{chr(97 + indice).upper()}) {valor}')

resposta = input('\nDigite apenas a opção: ')
if resposta.upper() == 'B':
    print('Certa resposta! ✅\n')
    acertos += 1
else:
    print('Errou ❌\n')

print(f'Você acertou {acertos} de 3 questões.\n\n\n')





# SEGUNDA VERSÃO

print('\tQUESTIONÁRIO\n')

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': ['4', 'c'],
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': ['25', '10'], # teste com menos alternativas
        'Resposta': ['25', 'a'],
    },
    {
        'Pergunta': 'Quanto é 10 dividido por 2?',
        'Opções': ['4', '5', '2', '1', '3', '7'], # teste com mais alternativas
        'Resposta': ['5', 'b'],
    },
    {
        'Pergunta': 'Qual é a linguagem de\nprogramação que tem nome de cobra?',
        'Opções': [], # teste sem alternativas
        'Resposta': ['python'],
    },
    {
        'Pergunta': 'Qual é o resultado de 12 - 6?',
        'Opções': [],
        'Resposta': ['6'],
    },
]

# i = índice das perguntas | j = índice das opções/alternativas

# Inicializa o contador de acertos
acertos = 0

# Loop principal para percorrer todas as perguntas
for i, pergunta in enumerate(perguntas):
    # Exibe a pergunta atual
    print(f'Questão {i + 1}: {pergunta["Pergunta"]}')
    
    # Loop para exibir todas as opções de resposta
    for j, alternativa in enumerate(pergunta['Opções']):
# chr(97 + j) converte o índice (0, 1, 2, ...) para as letras 'A', 'B', 'C', ...
        print(f'{chr(65 + j)}) {alternativa}')
    
    # Recebe a resposta do usuário e converte para minúscula
    resposta = input('\nSua resposta: ').lower()
    
    # Verifica se a resposta está na lista de respostas válidas
    if resposta in pergunta['Resposta']:
        print('Certa resposta! ✅\n')
        acertos += 1  # Incrementa o contador de acertos
    else:
        print('Errou ❌\n')

# Exibe o número total de acertos
print(f'Você teve um total de {acertos} de {len(perguntas)} acertos.\n')
