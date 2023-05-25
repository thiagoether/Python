dados = list()
pessoas = list()
pesado = leve = 0

while True:
    dados.append(str(input('Nome:')).capitalize().strip())
    dados.append(float(input('Peso:')))
    if len(pessoas) == 0:
        pesado = dados[1]
        leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        elif dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    op = str(input('Quer continuar? [s/n]:'))
    if op in 'Nn':
        break

print('-='*30)
print(f'No total foram cadastradas {len(pessoas)} pessoa(s).')

#mostrando pessoas mais pesadas
print('Pessoas mais pesadas:', end='')
for p in pessoas:
    if p[1] == pesado:
        print(p[0], end=' ')

#mostrando pessoas mais leves
print('\nPessoas mais leves:', end='')
for p in pessoas:
    if p[1] == leve:
        print(p[0], end=' ')