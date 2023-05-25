n = int(input('Digite um numero entre 1 e 10:'))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))