from random import randint
ale = randint(0,10)
qtd = 0

print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*10)

while True:
    n = int(input('Diga um valor:'))
    poi = str(input('Par ou ímpar? [p/i]')).strip().lower()
    if (n+ale) % 2 == 0:
        tipo = 'PAR'
    else:
        tipo = 'ÍMPAR'

    print('=-' * 20)
    print(f'Você jogou {n} e o computador {ale}. total de {n + ale} DEU {tipo}')
    print('=-' * 20)

    if (n+ale)%2 == 0 and poi == 'p':
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-'*20)
        qtd += 1
    else:
        print('Você PERDEU!')
        print('=-'*20)
        print(f'GAME OVER! Você venceu {qtd} vezes\n')
        break
