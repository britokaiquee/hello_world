import importlib

import recarregando_m

print(recarregando_m.variavel)

for i in range(10):
    importlib.reload(recarregando_m)
    # print(i)

print('Fim')