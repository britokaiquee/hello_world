# Closure e funções que retornam outras funções


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# Sem chamada imediata: Você cria a função aninhada e a armazena em uma variável
# para usar mais tarde.
print(falar_boa_noite('João'))
print()

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
print()

# Com chamada imediata, você chama a função retornada imediatamente:
falar_boa_noite2 = criar_saudacao('Boa noite')('Kaique')
print(falar_boa_noite2)

# O número de pares de parênteses depende de quantas vezes você está chamando
# funções em sequência. Cada par de parênteses representa uma chamada de função.
# E as chamadas de funções aninhadas devem ser chamadas na ordem certa.
