# O que é JSON?
# https://www.youtube.com/watch?v=XmCrArtfjaQ


import json

pessoa = {
    'nome': 'Kaique',
    'sobrenome': 'Brito ',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('arquivo.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
# para corrigir sobre os caracteres especiais, mas o professor manteria sem
# (ou seja True)
        ensure_ascii=False,
        indent=2,  # Para ficar formatado, e não na mesma linha
    )

with open('arquivo.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
