print('-'*30)
print('            BANCO')
print('-'*30)

valor = int(input('Que valor você quer sacar? R$'))

cem = int(valor / 100)
valor = valor % 100

cinquenta = int(valor / 50)
valor = valor % 50

vinte = int(valor / 20)
valor = valor % 20

dez = int(valor / 10)
valor = valor % 10

cinco = int(valor / 5)
valor = valor % 5

dois = int(valor / 2)
valor = valor % 2

um = valor


print(f'Cedulas de 100:{cem}')
print(f'Cedulas de 50:{cinquenta}')
print(f'Cedulas de 20:{vinte}')
print(f'Cedulas de 10: {dez}')
print(f'Cedulas de 5:{cinco}')
print(f'Cedulas de 2:{dois}')

