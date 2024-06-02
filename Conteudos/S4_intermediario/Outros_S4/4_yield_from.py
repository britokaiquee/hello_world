# Yield from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


# Alternativa: deixar vazio, colocar yield from gen1() e a variável g1 = gen2
def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:  # Alternativa: tirar o if e o " =None " do parâmetro
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
# Alternativa: g1 = gen2(gen1) | tirar o parêntese interior e colocar no
# yield from da função gen2, ou seja, executar ele na função invés de
# diretamente aqui

g2 = gen2(gen3())

g3 = gen2()


for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()