"""
Break: Usado para interromper imediatamente um loop (por exemplo, for ou while)
quando uma condição é atendida.
Ele quebra o laço.

Continue: Utilizado para pular parte do código dentro de um loop e
continuar com a próxima iteração, sem interromper o loop.
Ele pula uma parte do laço.
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
    # alternativa: 10 <= contador <= 27
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')