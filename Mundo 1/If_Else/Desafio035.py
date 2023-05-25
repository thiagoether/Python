s = float(input('Informe o salário:'))

if s > 1250:
    print('Salario com  aumento de 10%: R${:.2f}'.format(s * 1.10))
else:
    print('Salário com aumento de 15%: R${:.2f}'.format(s * 1.15))