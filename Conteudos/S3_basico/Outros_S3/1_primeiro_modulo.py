"""
Meu primeiro módulo Python (.py)

Obs: os comentários e docstrings foram colocados depois.
"""

# Para separar as coisas no terminal
print('-'*50)


print(12, 34, 1011, end='teste\n')
print(56, 78, sep='-', end='b\na')
print(9, 10, sep='', end='\n#')

print (1,'1teste 1 "testando" "teste"', 'testando',)


print('-'*50)


# type é usado para saber o tipo do objeto (em Python tudo é um objeto)
print(       type ('')          )
print(       type (1)           )
print(       type (0)           )
print(       type (-1)          )
print(       type (1.1)         )
print(       type (1.-1)        )
print(       type (-1.1)        )
print(       type (-1.-1)       )
print(type (-1.-1), type (1), type (""))

'''
== é usado para comparar se dois objetos têm o mesmo valor.
Ele pode ser usado tanto com tipos numéricos como inteiros e floats,
quanto com strings.
'''


print('-'*50)


# Outros testes (bagunça):
print(11 == 10)
print(type (1-1))
print(type (10==10))
print(0 ==0)
print(0== 1, 1==0)
print(1 == 1)
print(type (True), type(True))
print(type (True))
print(type (False))
print(1+1)
print(type (type))
print (5*2.5, 20/4, 30-5)
print ('a'+'b', '1'+'2')
print (str(3)+"D")
print (int ("10"), type ('1'), type(int('7')))
print (int ('1') + 1, float (1.1)+10, type (1.1))
print (bool (' '), bool (''), bool(), bool)
nome_completo = 'Kaique Brito'
soma_dois_mais_dois=2.5+2.5
int_um = bool('1')
print (int_um, '7', type(int_um))
print (nome_completo, soma_dois_mais_dois)
int_um = int('1')
print (int_um)


print('-'*50)


nome = 'Kaique'
idade = 19
maior_de_idade = idade >= 18
print (nome, idade, maior_de_idade)
print ('Nome:',nome,'Idade:',idade)
print ('É maior de idade?', maior_de_idade)

divisão = 8/5
print(divisão)