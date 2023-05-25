nome = input('Digite seu nome completo:').strip().title()
n = 'Silva' in nome
if n == True:
    print('Possui Silva no nome')
else:
    print('Não possui silva no nome')