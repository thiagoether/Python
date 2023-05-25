frase = str(input('Digite algo:')).strip().lower()
print('Quantas vezes apare a letra A: {}'.format(frase.count('a')))
print('Aparece a primeira vez na posição: {}'.format(frase.find('a') + 1))
print('Aparece por ultimo na posição: {}'.format(frase.rfind('a') + 1))
