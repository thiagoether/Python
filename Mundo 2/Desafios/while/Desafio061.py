pt = int(input('Informe o primeiro termo da PA:'))
r = int(input('Informe a razão da PA:'))
cc = 0
while cc < 10:
    print(pt)
    pt += r
    cc += 1

# METODO 2
# pt = int(input('Primeiro termo da PA:'))
# r = int(input('Razão da PA:'))
# c = 0
# while c < 10:
#    print(' {} '.format(pt), end='')
#    print('->' if c < 9 else 'FIM', end='')
#    pt += r
#    c += 1
