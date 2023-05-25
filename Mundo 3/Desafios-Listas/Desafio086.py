matriz = []

for l in range(3):
    for c in range(3):
        matriz.append(int(input(f'Digite um valor para [{l}, {c}]:')))

print('-='*30)

for l in range(3):
    print(f'[ {matriz[l]} ]', end='')
print('', end='\n')
for l in range(3, 6):
    print(f'[ {matriz[l]} ]', end='')
print('', end='\n')
for l in range(6, 9):
    print(f'[ {matriz[l]} ]', end='')

#SOLUÇÃO DE GUANABARA
#matriz = [[0,0,0],[0,0,0],[0,0,0]]
#for l in range(3):
#    for c in range(3):
#        matriz[l][c] = int(input(f'Valor [{l}, {c}]:'))
#print('-='*30)
#for l in range(3):
#    for c in range(3):
#        print(f'[{matriz[l][c]:^5}]', end='')
#    print()
