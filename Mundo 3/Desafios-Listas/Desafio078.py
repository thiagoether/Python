lista = []

for n in range(5):
    lista.append(int(input('Digite um valor:')))
print('=-'*20)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for p in range(len(lista)):
    if lista[p] == max(lista):
        print(f'{p}.. ', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for p in range(len(lista)):
    if lista[p] == min(lista):
        print(f'{p}.. ', end='')

