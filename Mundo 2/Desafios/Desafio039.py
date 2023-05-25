from datetime import date

ano_at = date.today().year

ano_nasc = int(input('Digite o ano de nascimento:'))
id = ano_at - ano_nasc

if id == 18:
    print('Você esta com idade para se alistar.')
elif id < 18:
    print('Você não tem idade para se alistar.')
    print('Faltam {} anos'.format(18 - id))
else:
    print('Passou da idade para o alistamento.')
    print('Se passaram {} anos'.format(id - 18))
