from random import randint
from time import sleep

dados = list()
jogo = list()

print('=' * 30)
print('      JOGA NA MEGA SENA')
print('=' * 30)

qtd_jogo = int(input('Quantos jogos você quer que eu sorteie?'))

for c in range(qtd_jogo):
    for c in range(6):
        dados.append(randint(1, 60))
    jogo.append(dados[:])
    dados.clear()
print(f'-=-=-= SORTEANDO {qtd_jogo} JOGOS -=-=-=')
for c in range(qtd_jogo):
    sleep(1)
    jogo[c].sort()
    print(f'Jogo {c + 1}: {jogo[c]}')
sleep(1)
print('-=-=-= < BOA SORTE > -=-=-=')

# DICA
# while True:
#    n = randint(1, 60)
#    if n not in lista:
#        lista.append(n)
