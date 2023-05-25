n = int(input('Digite um número inteiro qualquer:'))
base = int(input('# BASE DA CONVERSÃO #\n1-Binário\n2-Octal\n3-Hexadecimal'))
if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(oct(n)[2:])
elif base == 3:
    print(hex(n)[2:])
else:
    print('OPÇÃO INVÁLIDA !')