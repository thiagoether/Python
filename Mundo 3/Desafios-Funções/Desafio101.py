def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    id = ano_atual - ano
    if id < 16:
        print(f'Com {id} anos seu voto é negado!')
    elif (id >=16 and id < 18) or id > 65:
        print(f'Com {id} anos seu voto é opcional')
    else:
        print(f'Com {id} anos seu voto é obrigatório!')


anasc = int(input('Digite seu ano de nascimento:'))
voto(anasc)

