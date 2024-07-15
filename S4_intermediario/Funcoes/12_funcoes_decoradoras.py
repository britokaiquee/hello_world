'''
Funções decoradoras e decoradores

Decorar = Adicionar / Remover/ Restringir / Alterar
Funções decoradoras são funções que decoram outras funções.

Decoradores são usados para fazer o Python usar as funções decoradoras em outras
funções. E além disso, decoradores são "Syntax Sugar" (@syntax_sugar), que
traduzido pro português é "Açúcar Sintático".

Esse é o arquivo que mais fiz comentários até agora.
'''


# Definindo uma função decoradora chamada criar_funcao que recebe uma função
# como argumento
def criar_funcao(func):
    # Definindo uma função interna que será a função decorada
    def interna(*args, **kwargs):
        # Mensagem antes da função original, ou seja,
        # Adicionando (antes)
        print('Vou te decorar')  

        # Iterando sobre os argumentos posicionais, ou seja,
        # Restringindo
        for arg in args:
            # Verificando se cada argumento é uma string
            e_string(arg)

        # A váriavel abaixo chama a função original com os argumentos e captura
        # o resultado. É o equivalente a " resultado = inverte_string(string) "
        # dentro da função interna.

        # *args e **kwargs permitem flexibilidade na recepção de argumentos, 
        # aceitando qualquer quantidade de argumentos posicionais e nomeados.
        # Ou seja, sua variável pode receber o que quiser.
        resultado = func(*args, **kwargs)

        # Concatenando outra string ao resultado, ou seja,
        # Alterando
        resultado += " qualquer coisa"

        # Mensagem após a função original, ou seja,
        # Adicionando (depois)
        print('Ok, agora você foi decorada')

        # Comentando o que havia sido adicionado, ou seja,
        # Removendo
        # print(f'O seu resultado foi {resultado}.')

        # Retornando o resultado da função original
        return resultado
    # Retornando a função interna que agora está decorada
    return interna


# Utilizando a sintaxe de decorador @criar_funcao durante a definição da função
# inverte_string, em vez de decorá-la explicitamente após sua definição. E sem
# executar (sem os parênteses).
@criar_funcao
# Definindo uma função simples que inverte uma string
def inverte_string(string):
    # O print exibe o nome da função original antes de retornar a str invertida;
    # após a decoração com @criar_funcao, o nome exibido passa a ser "interna".
    # Pois o decorador as funções (no caso essa pela interna).
    print(f'{inverte_string.__name__}')
    return string[::-1]


# Definindo uma função que verifica se um parâmetro é uma string
def e_string(param):
    # Se o parâmetro não for uma string, levanta um erro
    if not isinstance(param, str):
        raise TypeError('o parâmetro deve ser uma string')


# Chamando a função decorada com uma string como argumento
invertida = inverte_string('123')
# Imprimindo o resultado da função decorada
print(invertida)


# Alternativa de decorador:

# # Decorando a função inverte_string com a função criar_funcao
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)