f = str(input('Digite uma frase:')).strip().lower()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É palindromo')
else:
    print('Não é palindromo')