from random import randint

lista = [0, 0, 0, 0, 0]
tupla = (lista)
maior = 0
menor = 0
cc = 0

for c in range(5): #preencher a lista
    lista[c] = randint(0, 10)
    maior = lista[0]
    menor = lista[0]

for c in range(5):
    if tupla[c] >= maior:
        maior = tupla[c]
    if tupla[c] <= menor:
        menor = tupla[c]


print(f'Listagem {tupla}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
