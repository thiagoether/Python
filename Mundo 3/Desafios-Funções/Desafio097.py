def mensagem(x):
    print('~'*(len(x)+4))
    print(f'{"  "}{x}')
    print('~'*(len(x)+4))


frase = str(input('Digite algo:'))
mensagem(frase)
