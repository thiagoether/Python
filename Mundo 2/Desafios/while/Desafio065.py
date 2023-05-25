contador = maior = menor = tot = 0
menu = 's'
vdc = True

while menu == 's':
    n = int(input('Informe um valor:'))
    contador += 1
    tot += n
    if vdc == True:
        menor = n
        vdc = False

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    menu = input('Continuar ou parar s/n ?')

print('Média:{}'.format(tot/contador))
print('Numeros Digitados:{}'.format(contador))
print('Maior:{}'.format(maior))
print('Menor:{}'.format(menor))








# Ler varios numeros inteiros
# Mostrar a media entre todos
# Mostrar o maior
# Mostrar o menor
# Perguntar se quer continuar ou não a digitar os valores