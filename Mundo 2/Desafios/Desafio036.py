vdc = float(input('Informe o valor da casa:'))
sal = float(input('Informe o salário do comprador:'))
t = int(input('Quantos anos para pagamento total?'))

ecd = sal * 0.30
p = vdc / (t*12)

if p > ecd:
    print('Emprestimo foi negado! Parcela muito alta!')
    print('Parcela:R${:.2f}'.format(p))
else:
    print('Emprestimo Aprovado!')
    print('Parcela: R${:.2f}'.format(p))

