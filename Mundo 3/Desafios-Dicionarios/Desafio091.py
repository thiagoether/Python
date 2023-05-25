from random import randint
from time import sleep
numeros = dict()
cc = 1

while True:
    ale = randint(1, 6)
    if ale in numeros.values():
        ale = randint(1, 6)
    else:
        numeros[f'jogador{cc}'] = ale
        cc += 1
    if cc == 5:
        break

print('Valores sorteados:')
for k, v in numeros.items():
    sleep(1)
    print(f'{k:>11} tirou {v}')
sleep(1)
cc = 1
print('Ranking dos jogadores:')
for n in sorted(numeros, key = numeros.get, reverse=True):
    sleep(1)
    print(f'{cc:>4}º lugar: {n} com {numeros[n]}')
    cc += 1