# Exercício 24 - Adiando execução de funções
# Solução melhor do professor no final

# Essa definição inteira (a linha abaixo) é chamada de assinatura da função, ou
# método também
def criar_funcao_somar(x):
    def somar(y):
        return x + y
    return somar


def criar_funcao_multiplicar(x):
    def multiplicar(y):
        return x * y
    return multiplicar


def executa(funcao, *args):
    return funcao(*args)


# Parâmetros x
soma_com_cinco = executa(criar_funcao_somar, 5)
multiplica_por_dez = executa(criar_funcao_multiplicar, 10)


# Parâmetros y
print(soma_com_cinco(2))
print(multiplica_por_dez(8))



# Sem a função criar_funcao:


def somar(x):
    def soma(y):
        return x + y
    return soma


def multiplicar(x):
    def multiplica(y):
        return x * y
    return multiplica


soma_com_5 = somar(5)
multiplica_por_10 = multiplicar(10)

print(soma_com_5(-2))
print(multiplica_por_10(1))



# Solução do professor:


def somando(x, y):
    return x + y


def multiplicando(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(somando, 5)
multiplica_por_dez = criar_funcao(multiplicando, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(8.5))