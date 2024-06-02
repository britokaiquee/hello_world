# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


# Criando um set
# set(iterável) ou {1, 2, 3}

set1 = set('Luiz')
set1 = set()  # vazio
set1 = {'Luiz', 1, 2, 3}  # com dados


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
set2 = set(l1)
l2 = list(set2)
set2 = {1, 2, 3}
print(3 not in set2)
print()
for numero in set2:
    print(numero)


# Métodos úteis:
# add, update, clear, discard
# s0 = set()
# s0.add('Luiz')
# s0.add(1)
# s0.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s0.discard('Olá mundo')
# s0.discard('Luiz')
# print(s0)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

print()
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s4 = s1 & s2
print(s4)
s5 = s1 - s2
print(s5)
s6 = s2 - s1  # inverso
print(s5)
s7 = s1 ^ s2
print(s6)



# Exemplo de uso dos sets (professor):

letras = set()
while True:
    letra = input('\nDigite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)



# Teste que eu fiz:

letras = set()
while True:
    letra = input('\nDigite: ')

# Não precisa colocar " == True " porque isalpha já é um bool True, e colocar
# == False faz aceitar qualquer caractere excerto letras, e o mesmo vale pra
# isdigit (qualquer caractere excerto números).
    if len(letra) == 1 and letra.isalpha():
        letras.add(letra.upper())
        # O espaço no end é a mesma coisa de pôr no final da str
        print('Letras usadas:', end=' ')
        print(*letras, sep=', ')

    else:
        print('Digite uma letra.')

    if 'L' in letras:
        print('PARABÉNS')
        break
