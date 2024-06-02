# Variáveis livres + nonlocal (locals, globals)

# Mostra todas variáveis globais definidas
print(globals())
print()

def fora(x):
    a = x

    def dentro():
        # Mostra as variáveis acessíveis dentro da função
        print(locals())
        print()

        # Mostra as funções livres dentro da função
        print(dentro.__code__.co_freevars)
        print()

        return a
    return dentro


dentro1 = fora(10)
# dentro2 = fora(20)

print(dentro1())
print()
# print(dentro2())
print()




def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # "nonlocal" é usado para acessar a variável da função externa
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)