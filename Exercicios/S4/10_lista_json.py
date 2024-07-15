# Exercício 28 - Passando a lista para um arquivo JSON

import json
import os


task_list = []
tasks_removed_list = []


def list_display():
    if task_list == []:
        print('\t   TAREFAS:\n')
        print('\t Lista vazia.')

    else:
        print('\t   TAREFAS:\n')
        for indice, task in enumerate(task_list, start=1):
            print(f'{indice}. {task}')


def execute_command():
    if command == 'desfazer':
        try:
            os.system('cls')
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
        if command != '':
            os.system('cls')
            task_list.append(command)
        else:
            os.system('cls')
            print('Você não digitou nada.\n')


while True:
    list_display()

    command = input(
        '\nComandos: desfazer | refazer \
         \nDigite uma tarefa ou comando: '
    )

    execute_command()

    with open('teste1.json', 'w', encoding='utf8') as teste1:
        json.dump(
            task_list,
            teste1,
            ensure_ascii=False,
            indent=2
        )

    with open('teste1.json', 'r', encoding='utf8') as teste1:
        list_json = json.load(teste1)
        print('\t•ARQUIVO JSON•\n')
        print(*list_json, sep='\n')
        print('\n'*2)



# Solução do professor (comente tudo acima para testar)

import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'lista_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

# A versão do professor deixa apenas a lista do arquivo json, podendo excluir
# tarefas da lista diretamente no arquivo, e fazendo excluir no terminal também.