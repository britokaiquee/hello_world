# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# try:
#     import sys

#     sys.path.append('/Users/Kaique/Desktop/')

# except ModuleNotFoundError:
#     ...

#     print("O módulo 'sys' não foi encontrado.")

# print(*sys.path, sep="\n")


print('Este módulo se chama', __name__)



# Módulo inteiro

# import modularizacao_m

# print(modularizacao_m.variavel_modulo)
# print(modularizacao_m.soma(2, 3))


# import modularizacao_m as mod   # Com alias

# print(mod.variavel_modulo)
# print(mod.soma(2, 3))



# Partes do módulo

# from modularizacao_m import soma, variavel_modulo

# print(variavel_modulo)  
# print(soma(2, 3))


from modularizacao_m import soma as s, variavel_modulo as vm  # Com alias

'''
Alternativa:
from modularizacao_m import soma as s
from modularizacao_m import variavel_modulo as vm
'''

print(vm)
print(s(2, 3))