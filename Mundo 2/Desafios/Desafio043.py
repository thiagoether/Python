p = float(input('Informe o peso:'))
a = float(input('Informe a altura:'))

imc = p / (a*a)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')

print('{:.2f}'.format(imc))
