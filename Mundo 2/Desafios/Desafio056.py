tot_id = 0
hmv = 0
mmdv = 0
mi = 0
ndhmv = ''
mmn = 0
for c in range(0, 4):
    nome = str(input('Digite seu nome:'))
    id = int(input('Digite sua idade:'))
    s = str(input('Informe o sexo(M/F):'))
    tot_id += id
    if s == 'm' and id > mi:
        ndhmv = nome
    elif s == 'f' and id < 20:
        mmn += 1
print('Média de idade:{} anos'.format(tot_id / 4))
print('Homem mais velho:{}'.format(ndhmv))
print('Mulheres menores de 20 anos:{}'.format(mmn))
