lista = []

lista.append(str(input('Digite uma expressão:')))
if lista[0].count('(') == lista[0].count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')