# Exercício 3: Comparando valores

primeiro_valor = (input('Digite um valor: '))
segundo_valor = (input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo valor.')
        # alternativa: >= (maior ou igual)
elif primeiro_valor < segundo_valor:
        # alternativa: elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior que o primeiro valor.')
else:
    print('Os dois valores são iguais.')


# Upgrade
# Para ser só com números, e fazer comparação certa entre números negativos:

primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo valor.')
elif segundo_valor > primeiro_valor:  # Com a alternativa
    print('O segundo valor é maior que o primeiro valor.')
else:
    print('Os dois valores são iguais.')


# Upgrade 2
# Com mensagem de erro / Para repetir infinitamente:

while True:
    try:
        primeiro_valor = float(input('Digite um valor: '))
        segundo_valor = float(input('Digite outro valor: '))

        if primeiro_valor > segundo_valor:
            print('O primeiro valor é maior que o segundo valor.')
        elif segundo_valor > primeiro_valor:  # Com a alternativa
            print('O segundo valor é maior que o primeiro valor.')
        else:
            print('Os dois valores são iguais.')
            # break

# O break serve para parar a repetição, e nesse caso ele para ao
# Inserir os valores corretamente
# Para parar a repetição sem precisar do break, use o atalho CTRL+C
# No terminal

    except ValueError:
        print("Valor inválido. Digite apenas números.")

# O bloco try e o bloco except dependem um do outro para funcionar.
