# Define uma string com espaços reservados para três valores.
string = '1={} 2={} 3={}'

# Preenche os espaços reservados com os valores 1, 2 e 3.
formato = string.format(1, 2, 3)
print(formato)

# Define três variáveis com valores diferentes.
a = 1.1
b = '2'
c = 'A'

formato2 = 'A={:.2f} B={} C={} {}'.format(a, b, c, '123')
print(formato2)

x = 3
y = 2.2
z = 'B'

formato3 = '1={0} 2={1:.2f} 3={1:.2f} 4={2} 5={teste}'.format(
    x, y, z, teste='456')
print(formato3)

# Define duas variáveis 'nome' e 'idade'.
nome = 'Kaique'
idade = '19'

# Formata uma string com espaços reservados para duas variáveis,
# preenchendo-os com os valores das variáveis 'nome' e 'idade'.
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = 'Kaique'
idade = '20'

# Formata uma string com espaços reservados para duas variáveis,
# preenchendo-os com os valores das variáveis utilizando nomes de argumentos.
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))



# Professor:
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)