"""
Operador ternário, também chamado de operação ternária
(condicional de uma linha)
<valor> if <condicao> else <outro valor>

exemplo:
numero = numero if numero <= 9 else 0
o número será ele mesmo se (if) for menor ou igual a 9,
do contrário (else) será 0.
"""


condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 10  # > 9 = 0

novo_digito = digito if digito <= 9 else 0
# alternativa: novo_digito = 0 if digito > 9 else digito

print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')
