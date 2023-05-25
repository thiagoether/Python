from datetime import date

aa = date.today().year
maior = 0
menor = 0

for c in range(0, 6):
    anasc = int(input('Informe o ano de nascimento'))
    if (aa - anasc >= 21):
        maior += 1
    else:
        menor += 1
print('Maiores de idade: {}\nMenores de idade: {}'.format(maior, menor))
