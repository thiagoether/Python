from random import randint
lista = [0, 0, 0, 0, 0]
tupla = (lista)
maior = 0
menor = 101

for c in range(5): # preencher a lista
    ale = randint(0, 100)
    lista[c] = ale
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]


print(f'Listagem: {tupla}')
print(f'Maior: {maior}')
print(f'Menor:{menor}')

