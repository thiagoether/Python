lista1 = list()

while True:
    n = int(input('Digite um numero:'))
    lista1.append(n)
    if n % 2 == 0:
        lpar = []
        lpar.append(n)
    else:
        limpar = []
        limpar.append(n)
    while True:
        op = str(input('Quer continuar? [s/n]'))
        if op == 's':
            break
        if op == 'n':
            break
    if op == 'n':
        break

print(f'A lista completa é {lista1}')
print(f'A lista de pares é {lpar}')
print(f'A lista de ímpares é {limpar}')