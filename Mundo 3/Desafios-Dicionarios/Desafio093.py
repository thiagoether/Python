jogador = dict()
gol = list()
lista = list()
tot = 0

jogador['nome'] = str(input('Nome do jogador:')).capitalize()
qp = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for c in range(qp):
    n = int(input(f'Quantos gols na partida {c}?'))
    gol.append(n)
jogador['gols'] = gol
#calculando o total de gols na lista:
for c in range(len(gol)):
    tot += gol[c]
jogador['total'] = tot

print('-='*30)
lista = jogador.copy()
print(f'{lista}')
print('-='*30)

for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}.', end='')
    print()
print('-='*3 0)
print(f'o jogador {jogador["nome"]} jogou {qp} partidas.')
for c in range(len(gol)):
    print(f'{"=>":>5} na partida {c}, fez {gol[c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
