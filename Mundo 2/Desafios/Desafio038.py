v1 = int(input('Informe o primeiro valor:'))
v2 = int(input('Informe o segundo valor:'))

if v1 == v2:
    print('Não existe valor maior, os dois são iguais.')
elif v1 > v2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior.')