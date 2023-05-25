c1 = 1
c2 = 0
exc = 1
fim = 10

pt = int(input('Informe o primeiro termo da PA:'))
r = int(input('Informe a razão da PA:'))

while c1 != 0:
    while c2 < fim:
        print(pt)
        pt += r
        c2 += 1
    exc = int(input('Voce deseja mostrar mais quantos valores?'))
    fim += exc
    c1 = exc

# METODO 2]
# pt = int(input('Primeiro termo:'))
# r = int(input('Razão:'))
# op = 10
# while op != 0:
#    for c in range(op):
#        print('{}'.format(pt), end='')
#        print(' -> ' if c < op-1 else '-> FIM', end='')
#        pt += r
#    op = int(input('\nQuantos termos você quer mostrar a mais?'))


# Progressão aritmetica
# perguntar ao usuario quantos termos ele quer mostrar a mais
# se digitar 0 o programa se encerra
