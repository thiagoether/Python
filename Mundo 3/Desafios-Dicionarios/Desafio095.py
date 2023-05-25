jogadores = list()
dados = dict()
gol = list()
tot = 0

qp = 0 #quantidade de partidas
while True:
    print('='*30)
    dados['nome'] = str(input('Nome: '))
    qp = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(qp):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
    for c in gol:
        tot += c
    dados['total'] = tot
    dados['gols'] = gol[:]
    gol.clear()
    tot = 0
    jogadores.append(dados.copy())

    op = str(input('Quer continuar? [S/N] ')).lower()
    if op in 'Nn':
        break


print('-='*30)
print(f'{"cod"}{"nome":>5}{"gols":>15}{"total":>15}')
print('='*40)
for c in range(len(jogadores)):
    print(f'{c:3} {jogadores[c]["nome"]:<14} {jogadores[c]["gols"]} {jogadores[c]["total"]:>3}')

print('='*40)

while True:
    d = int(input('Mostrar dados de qual jogador? '))
    if d == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[d]["nome"].capitalize()}')
    i = 0
    for j in jogadores[d]['gols']:
        print(f'No jogo {i} fez {j} gols.')
        i += 1
    print('='*40)

#MENSAGEM DE FIM
print('<< VOLTE SEMPRE >>')


