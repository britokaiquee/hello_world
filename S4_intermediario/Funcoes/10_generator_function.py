# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def gerador(n=0):
    yield 1  # Pausar
    return 'ACABOU'


gen = gerador(n=0)
print(gen.__iter__)
print(next(gen))



def contador():
    print("Iniciando")
    yield 1
    print("Interrompido")
    yield 2
    print("Interrompido novamente")
    yield 3
    print("Finalizando")
    # Esse return indica o fim do gerador e pode retornar um valor que só é
    # acessível através da exceção StopIteration, o que significa que ele é
    # redundante para o fluxo normal.
    return 'ACABOU'


gen = contador()

print(next(gen))  # Inicia e retorna 1
print(next(gen))  # Continua e retorna 2
print(next(gen))  # Continua e retorna 3
print(next(gen))  # Fim do gerador



def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:  # >= faz parar um número antes do limite, igual range
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)

# Mesma coisa que o range faz, sendo que se emitir o argumento n (ínicio/mínimo)
# por padrão ele começa do 0 também por causa do valor padrão que foi colocado
# pro parâmetro, e nesse caso o padrão do maximum (máximo) deve ser 10 também.
