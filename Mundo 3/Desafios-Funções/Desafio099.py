from time import sleep


def maior(*n):
    c = m = 0
    print('-=' * 20)
    print('Analizando os valores passados..', end='')
    for v in n:
        print(f'{v}', end=' ')
        if v > m:
            m = v
        sleep(0.4)
    print(f'\nForam informados {len(n)} valores ao todo..')
    print(f'O maior valor é: {m}')


maior(5, 5, 3, 8, 2)
maior(2, 4, 1, 7, 9, 12, -4, 0)
