"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#         velocidade > RADAR_1:
#     print('A velocidade do carro passou do radar 1')
#     print('O carro foi multado no radar 1')

# Deixando o código mais legível:

vel_passou_r1 = velocidade > RADAR_1
car_passou_r1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
car_multado_r1 = car_passou_r1 and vel_passou_r1

# if vel_passou_r1:
    # print('A velocidade do carro passou do limite do radar 1')

if car_passou_r1:
    print (f'O carro passou pelo radar 1 a {velocidade} km/h')

if car_multado_r1:
    print('A velocidade do carro ultrapassou o limite permitido')
    print('O carro foi multado')
    # print('O carro foi multado no radar 1')