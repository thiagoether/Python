i1 = int(input('Valor 1:'))
i2 = int(input('Valor 2:'))
i3 = int(input('Valor 3:'))
i4 = int(input('Valor 4:'))

tupla = (i1, i2, i3, i4)

print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) > 0:
    print(f'O numero 3 apareceu na {tupla.index(3)}º posição')
else:
    print('O numero 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for c in range(4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')