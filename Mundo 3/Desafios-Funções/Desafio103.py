def ficha(nome, gols):
    if nome == '':
        nome='<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do jogador:')
g = input('Número de gols:')
ficha(n, g)
