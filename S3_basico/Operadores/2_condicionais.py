# Operadores condicionais

# if / elif      / else
# se / se não se / se não



print('Fora do if')

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(12345)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nenhuma das opções')

print('Fora dos blocos')

condicao = False # o interpretador ignora o código do if quando está como False

if condicao:
    print('código do if 1')
else:
    print('código else do primeiro if')

if 10 == 10:
    print('código do if 2')

if 10 == 9: # Numéros diferentes = False, iguais = True
    print('outro código do if 2')

if False:
    print('código do if 3')

if True:
    print('código do if 4')

if False:
    print('código do if 5')



condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1.1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')