colocados = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
             'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

# LETRA A
print(colocados[:5]) # primeiros 5 colocados
# LETRA B
print(colocados[-4:]) # ultimos 4 colocados
# LETRA C
print(sorted(colocados)) # mostrar a lista em ordem alfabética
# LETRA D
print(colocados.index('Palmeiras')+1, end='º') # MOSTRAR A POSIÇÃO DE JUVENTUDE