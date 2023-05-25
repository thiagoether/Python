def leiaInt(frase):
    while True:
        v = input(frase)
        if v.isnumeric() == True:
            print(f'Você acabou de digitar o numero {v}')
            break
        else:
            print('ERRO! digite um número válido.')



n = leiaInt('Digite um numero: ')

