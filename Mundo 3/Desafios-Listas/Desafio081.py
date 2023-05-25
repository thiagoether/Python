lista = []

while True:
    lista.append(int(input('Digite um valor:')))
    while True:
        op = str(input('Quer continuar? [s/n]'))
        if op == 'n':
            break
        if op == 's':
            break
    if op == 'n':
        break
print('='*30)
print(f'Você digitou {len(lista)} elemento(s)')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')