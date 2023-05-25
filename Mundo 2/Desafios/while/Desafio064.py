n = soma = tot = 0
while n != 999:
    n = int(input('Digite um numero(999 para parar):'))
    if n == 999:
        break
    else:
        soma += n
        tot += 1
print('Você digitou {} numeros e a soma total é:{}'.format(tot, soma))