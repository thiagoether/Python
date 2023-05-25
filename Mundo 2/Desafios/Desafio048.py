s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        if n % 2 == 1:
            s += n
print('A soma entre todos os impares e multiplos de 3 é: {}'.format(s))
