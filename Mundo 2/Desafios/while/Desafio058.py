import random

tentativas = 0
while True:
    tentativas += 1
    ale = random.randint(0, 10)
    n = int(input('Digite um número:'))
    if ale == n:
        print('VOCÊ ACERTOU! Com {} tentativas'.format(tentativas))
        break
    else:
        print('ERROU')


# METODO 2
# from random import randint

# ale = randint(0,10)
# tentativas = 1

# print('Sou seu computador..\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
# n = int(input('Qual é seu palpite?'))

# while n != ale:
#    n = int(input('Mais... tente mais uma vez.\nQual é seu palpite?'))
#    tentativas += 1
# print('Acertou com {} tentativas. Parabéns!'.format(tentativas))