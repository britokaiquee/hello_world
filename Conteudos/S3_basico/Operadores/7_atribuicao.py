"""
Operadores de atribuição com operadores aritméticos:
= += -= *= /= //= **= %=
"""

contador1 = 10
contador1 += 15
print(contador1)

contador2 = 10
contador2 -= 15
print(contador2)

contador3 = 10
contador3 *= 2
print(contador3)

contador4 = 10
contador4 //= 5 # número inteiro (int)
print(contador4)

contador5 = 10
contador5 /= 5 # número flutuante (float)
print(contador5)

contador6 = 10
contador6 **= 3
print(contador6)

contador7 = 10
# outra forma de saber se o número é par, que é vendo se o resultado é 0
# ou seja, não teve resto
contador7 %= 2
print(contador7)

#####

concatenacao1 = 'Kaique'

concatenacao1 += ' Brito'
print(concatenacao1)

concatenacao2 = 'a'

concatenacao2 *= 12
print(concatenacao2)

#####

contagem = 1

while contagem <= 10:
    print(contagem)
    contagem += 1
