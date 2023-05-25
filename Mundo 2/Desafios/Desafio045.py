import random

user = int(input('Digite sua escolha:\n1-Pedra\n2-Papel\n3-Tesoura\n->'))
lista = ['Pedra', 'Papel', 'Tesoura']
ale = random.randint(0, 2)
ale += 1

if ale == user:
    print('Empate!')
elif ale == 1 and user == 2:
    print('Ganhou! Papel ganha de pedra.')
elif ale == 1 and user == 3:
    print('Perdeu! Pedra ganha de tesoura.')
elif ale == 2 and user == 1:
    print('Perdeu! Papel ganha de pedra.')
elif ale == 2 and user == 3:
    print('Ganhou! Tesoura ganha de pepel.')
elif ale == 3 and user == 1:
    print('Ganhou! Pedra ganha de tesoura.')
else:
    print('Perdeu! Tesoura ganha de papel.')

print('Escolha do Usuário: {}'.format(user))
print('Escolha do computador: {}'.format(ale))


