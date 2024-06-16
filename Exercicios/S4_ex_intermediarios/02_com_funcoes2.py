# Exercício 18
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


# v1

def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero * 3

def quadruplo(numero):
    return numero * 4

num1 = dobro(2)
num2 = triplo(2)
num3 = quadruplo(2)

print(num1, num2, num3)


# v2

def numeros(x, y, z):
    return x * 2, y * 3, z * 4

resultados = numeros(1, 1, 1)

print(*resultados)


# v3

def duplica(numero):
    return numero * 2

def triplica(numero):
    return numero * 3

def quadruplica(numero):
    return numero * 4

numero = 5
print("Duplicado:", duplica(numero))
print("Triplicado:", triplica(numero))
print("Quadruplicado:", quadruplica(numero))


# v4

def multiplicacao(numero, multiplicador):
        return numero * multiplicador

print(multiplicacao(3, 2))
print(multiplicacao(3, 3))
print(multiplicacao(3, 4))

# v = versão


# Solução do professor

# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))