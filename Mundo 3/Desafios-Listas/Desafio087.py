matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = impar = svtc = mvsl = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares é {par}')
for l in range(3):
    svtc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {svtc}')
for c in range(3):
    if matriz[1][c] > mvsl:
        mvsl = matriz[1][c]
print(f'O maior valor da segunda linha é {mvsl}')