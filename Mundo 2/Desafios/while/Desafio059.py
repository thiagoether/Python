menu = True
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo Valor:'))

while menu:
    op = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair\nSua opção:'))
    if op > 5 or op < 1:
        op = int(input('Opção inválida!\nDigite sua opção:'))
    elif op == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, (n1+n2)))
        print('='*24)
    elif op == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, (n1*n2)))
        print('=' * 26)
    elif op == 3:
        if n1 == n2:
            print('{} é igual a {}'.format(n1, n2))
        elif n1 > n2:
            print('O número {} é o maior'.format(n1))
            print('=' * 25)
        else:
            print('O numero {} é o menor'.format(n2))
            print('='*25)
    elif op == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    else:
        break

