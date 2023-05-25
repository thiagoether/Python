import datetime

date = datetime.date.today()
year = date.strftime("%Y")
anasc = int(input('Informe o ano de nascimento:'))
id = int(year) - anasc

if id <= 9:
    print('CATEGORIA MIRIM')
elif id > 9 and id <= 14:
    print('CATEGORIA INFANTIL')
elif id > 14 and id <= 19:
    print('CATEGORIA JUNIOR')
elif id > 19 and id <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')