n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))

m = (n1 + n2) / 2

if m >= 7:
    print('APROVADO!')
    print('Média:{:.1f}'.format(m))
elif m >= 5 and m <=6.9:
    print('RECUPERAÇÃO!')
    print('Média:{:.1f}'.format(m))
else:
    print('REPROVADO!')
    print('Média:{:.1f}'.format(m))