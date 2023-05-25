s = str(input('Digite o seu sexo M/F:')).strip().upper()
while s not in 'MF':
    s = str(input('Entrada inválida! Digite novamente o seu sexo:')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(s))