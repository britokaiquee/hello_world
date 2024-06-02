# Decoradores com parâmetros

# Primeira função: pra pegar os parâmetros do decorador
def fabrica_de_decoradores(a=None, b=None, c=None):  # Nome anterior: decoradora

    # Segunda função: pegar a função (então é o decorador em si)
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        # Terceira função: é a sua função que você vai executar.
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funcoes


# o decorador passa a função abaixo como argumento do parâmetro da função em
# que ele foi especificado
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)



# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} | {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5º')
@parametros_decorador(nome='4º')
@parametros_decorador(nome='3º')
@parametros_decorador(nome='2º')
@parametros_decorador(nome='1º')
def soma(x, y):
    return x + y


soma_dez_mais_cinco = soma(10, 5)
print(soma_dez_mais_cinco)