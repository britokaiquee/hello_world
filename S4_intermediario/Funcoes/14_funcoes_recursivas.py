# Funções recursivas e recursividade

# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores

# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        # Antes aqui era "fim", mas deixei uma str vazia para não aparecer
        # nada (se deixar return vazio aparece none)
        return ''

    # Caso recursivo (recursividade)
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)  # Recursão (quando a função chama a si mesma)


print(recursiva())  # É como se fosse um loop (fazendo iteração)