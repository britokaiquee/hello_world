"""
Isso é uma DocString, e serve para escrever anotações (documentações)
É feita com 6 aspas do mesmo tipo: simples ou duplas (nesse caso ambas chamadas
de aspas triplas).

É recomendado que a docstring seja colocado acima da definição da função quando
houver.

Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas

# \r\n -> CRLF
# \n -> LF
"""

''' Também pode ser usado assim '''

# A hashtag permite escrever um comentário, seja acima
print(123)  # Na frente
# Abaixo
print(456)

print(1234)


# String (str) de aspas simples:
print('Kaique Brito')
print(1, 'Kaique "Brito"')

# Aspas duplas:
print("Kaique Brito")
print(2, "Kaique 'Brito'")

# Escape:
print("Kaique \"Brito\"")

'''
As barras invertidas "\", são para poder usar as mesmas aspas da string invés de
usar o outro tipo e o "r" antes da string é para que as sequências de escape
(como "\" e "\n" por exemplo) apareçam ao ser imprimido. Obs: as vírgulas entre
os argumentos na função print sempre ficam invísiveis mesmo, pois ela é apenas
para separar os argumentos.
'''

# r
print(r"Kaique \"Brito\"")

'''
Deixar o "r" maiúsculo antes da string fará com que os caracteres como aspas e
sequências de escape não tenham destaque, que seriam as cores diferentes, como
vermelho no caso das aspas e rosa no caso das sequências de escape. O "\n"
maiúsculo continua com o destaque rosa quando está com o "r" no início da
string. Porém o prefixo "r" desativa os escapes, no caso do \n, \t,
etc. Ele também funciona maiúsculo "R" e é chamado de raw string (string crua).

Atualização: Dá pra colocar f-string com o "F" maiúsculo também (sem nenhuma
mudança), assim como no caso das strings literais com o "R" maiúsculo. Já outros
escapes coomo os que são acompandados de uama barra invertida só funcionam com
a letra minúscula.
'''

print("teste\"teste2\"")
print('teste\'teste2\'') # Inverso
print(r"teste\"teste2\"")

# Alternativa com outro tipo de aspas diferente da utilizada para a string, na
# qual deixa o código mais limpo:
print("teste 'teste2' ")

# \n
print('\n', 1, 2, 3, end='___separador___')

'''
"\n" é usado como quebra de linha, o que significa que no terminal o conteúdo
antes do "\n" permanecerá na mesma linha, enquanto que o conteúdo após irá para
a próxima. Colocando no início da string ele dá o espaço vazio acima da linha, e
no final ele dá o espaço após. Além de que ele não é exibido no terminal, a
menos que use "r" antes da string.
'''

# end
print('\n', 1, 2, 3, end='___separador___')

"""
O argumento "end=" determina o que será adicionado no final da saída da
função print(). Se utilizado "end=" seguido de "\n", isso é equivalente a
simplesmente adicionar "\n" ao final. Contudo, para produzir um salto de
linha sem que o "end=" anule esse salto, é necessário adicionar dois "\n",
ou seja, " end="\n\n" ".

Enquanto o "\n" separa as linhas, o "end" as une, atuando como um conector
entre elas. Se "end" estiver vazio, não haverá nenhuma separação adicional
entre as saídas.

É importante observar que o "end" só pode ser utilizado no final da função
print, e que não poderá ter mais nada após ele.
"""

print(4, 5, 6, sep="-", end="")

'''
"sep=" é o separador de argumentos da função print (sejam eles str, int, float,
variavel, etc), sendo que não separa se não houver
nada entre as aspas dele.
'''

print(7, 8, sep='', end='fim\n')
