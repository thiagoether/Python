lista = []

while True:
    v = int(input('Digite um valor:'))
    if v in lista:
        print('Valor duplicado! Não vou adicionar..')
    else:
        print('Valor adicionado com sucesso..')
        lista.append(v)
    while True:
        op = str(input('Quer continuar? [s/n]'))
        if op == 's':
            break
        elif op == 'n':
            break
    if op == 'n':
        break
lista.sort()
print('=-'*40)
print(f'Você digitou os valores {lista}')