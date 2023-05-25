print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)
total = 0
pmm = 0
pmb = 0
npmb = ''

while True:
    produto = input('Nome do produto:')
    preco = float(input('Preço: R$'))
    total += preco

    if pmb == 0:
        pmb = preco
    if preco <= pmb:
        pmb = preco
        npmb = produto

    if preco > 1000:
        pmm += 1

    while True:
        op = str(input('Quer continuar? [s/n]')).strip().lower()
        if op == 's' or op == 'n':
            break

    if op == 'n':
        print('=' * 5 + 'FIM DO PROGRAMA' + '=' * 5)
        print(f'O total da compra foi R${total:2}')
        print(f'temos {pmm} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {npmb} que custa R${pmb}')
        break
