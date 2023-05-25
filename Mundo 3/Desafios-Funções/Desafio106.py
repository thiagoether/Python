from time import sleep
menu = 'SISTEMA DE AJUDA PyHELP'
msg = 'Acessando o manual do'
msgf = 'ATÉ LOGO!'



def ajuda(funcao):
    print(help(op))


while True:
    print('\033[0;29;42m~\033[m' * (len(menu)+4))
    print('\033[0;29;42m  SISTEMA DE AJUDA PyHELP\033[m', end='\033[0;29;42m \033[m')

    print('\033[0;29;42m~\033[m'*(len(menu)+4))
    op = str(input('Função da biblioteca > '))
    if op == 'fim':
        print('~'*(len(msgf)+4))
        print(f'  {msgf}')
        print(f'~'*(len(msgf)+4))
        break
    sleep(0.5)
    print('~' * (len(msg) + 4))
    print(f'  {msg} {op}')
    print('~' * (len(msg) + 4))
    sleep(0.5)
    ajuda(op)



