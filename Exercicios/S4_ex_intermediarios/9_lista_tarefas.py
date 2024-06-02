# Exercício 27 - Lista de tarefas com desfazer e refazer

# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


import os

task_list = []
tasks_removed_list = []  # Para ao usar o comando de refazer, não refazer tudo


def list_display():
    if task_list == []:
        print('TAREFAS:')
        print('Lista vazia.')

    else:
        print('TAREFAS:')
        for task in task_list:
            print(f'\t{task}')


def execute_command():
    if command == 'desfazer':
        try:
            os.system('cls')  # Tem outras formas de limpar além dessa
            task_removed = task_list.pop()
            tasks_removed_list.append(task_removed)
        except IndexError:
            os.system('cls')
            print('Não há nada para desfazer.\n')

    elif command == 'refazer':
        try:
            os.system('cls')
            task_removed = tasks_removed_list.pop()
            task_list.append(task_removed)
        except IndexError:
            os.system('cls')
            print('Não há nada para refazer.\n')

    else:
        os.system('cls')
        task_list.append(command)


while True:
    list_display()

    command = input(
        '\nComandos: desfazer | refazer \
         \nDigite uma tarefa ou comando: '
    )

    execute_command()



# Solução do professor (comente tudo acima para testar)

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} readicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue