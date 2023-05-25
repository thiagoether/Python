maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Informe o peso:'))

    if peso > maior:
        maior = peso
    else:
        menor = peso

print(maior)
print(menor)