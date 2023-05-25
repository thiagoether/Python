tdh = 0
tdmmv = 0
m18 = 0

while True:
    print('-' * 30 + '\nCADASTRE UMA PESSOA\n' + '-' * 30)
    i = int(input('Idade:'))
    while True:
        s = str(input('Sexo: [M/F]')).strip().lower()
        if s == 'm' or s == 'f':
            if s == 'm':
                tdh += 1
            if s == 'f' and i < 20:
                tdmmv += 1
            if i > 18:
                m18 += 1
            break


    while True:
        op = str(input('Quer continuar? [s/n]'))
        if op == 's' or op == 'n':
            break
            tot += 1
    if op == 'n':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos:{m18}')
print(f'Ao todo temos {tdh} homens cadastrados')
print(f'E temos {tdmmv} mulher(es) com menos de 20 anos')
