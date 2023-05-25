while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 25)
    if n < 0:
        print('Programa tabuada encerrado. Volte sempre!')
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 25)