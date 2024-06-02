# Operadores lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser verdadeiras
# or -  Pelo menos uma das condições precisa ser verdadeira
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 | 0.0 | '' (string vazia) --> Falsy (False)
# E truthy o contrário disso, como um número diferente de zero
# Ou uma string com conteúdo
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and True)
print(False and False)
# Com 'and', o resultado para no 1º Falsy (se tiver), ou Falsy
# E exibe esse valor. Caso contrário, se não tiver, o que será exibido será
# O último True ou Truthy (contrário de Falsy)
print(True and False and True)
print(True and 0 and True) 
print(False or False)
print(True or True)
# Já com o 'or' é o contrário, o resultado para no 1º True ou Truthy (se tiver)
# E exibe esse valor. Caso contrário, se não tiver, o que será exibido será
# O último False ou Falsy
print(True and False and True)
print(False or True or False)
print(False or '' or 1)

senha = input('Senha: ') or 'Sem senha'
print(senha)

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True
