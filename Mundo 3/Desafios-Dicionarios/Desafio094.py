pessoas = list()
dados = dict()
tot = m = 0

while True:
    dados['nome'] = str(input('Nome:')).capitalize()
    while True:
        dados['sexo'] = str(input('Erro, Digite novamente! Sexo: [M/F] ')).upper()
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input('Idade:'))
    pessoas.append(dados.copy())
    op = str(input('Quer continuar? [S/N] ')).lower()
    if op in 'nN':
        break

print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoa(s).')

# media de idade:
for p in pessoas:
    tot += p['idade']
m = tot/len(pessoas)
print(f'- A média de idade é de {m} anos.')

#mostrando as mulheres cadastradas:
print(f'- As mulheres cadastradas foram: ',end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')

#lista de pessoas que estão acima da média
print('\n- Lista de pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > m:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')
        print()
print('<< ENCERRADO >>')