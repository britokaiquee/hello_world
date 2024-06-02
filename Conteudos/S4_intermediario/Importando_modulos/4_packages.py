# from sys import path

# import package.modulo
# from package import modulo
# from package.modulo import *  # dá para usar __all__

# # from package.modulo import soma_do_modulo  # aula99

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)


# from package.modulo import fala_oi, soma_do_modulo

'''
__name__ é pra saber o nome do módulo se tiver sido importado, se for o
atual retorna __main__
'''
# print(__name__)
# fala_oi()


from package import fala_oi, soma_do_modulo

print(soma_do_modulo(2, 3))
fala_oi()

# O ideal é pôr o módulo main (principal) na raiz, ou seja, na pasta mãe. Pra
# depois fazer as importações.

# Aqui estou deixando nessa pasta pra ficar organizado as pastas de conteúdos.