import random

ale = random.randint(0, 5)
pal = int(input('Palpite:'))
#METODO 1
print('Acertou!' if pal==ale else 'Errou!')
#METODO 2
if pal == ale:
    print('Acertou!')
else:
    print('Errou!')
