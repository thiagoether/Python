npe = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero entre 0-20:'))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    else:
        break

print(f'Você digitou o número {npe[n]}')
