p = float(input('Digite o preço do produto:'))

print('# FORMAS DE PAGAMENTO #')
print('1- À Vista no dinheiro/cheque (10% de desconto)')
print('2- À Vista no cartão(5% de desconto)')
print('3- 2x no cartão (SEM DESCONTO)')
print('4- 3x ou mais no cartão (20% de juros)')

op = int(input('Opção selecionada:'))

if op == 1:
    print('Desconto de 10%: Valor final R${:.2f}'.format(p * 0.9))
elif op == 2:
    print('Desconto de 5%: Valor final R${:.2f}'.format(p * 0.95))
elif op == 3:
    print('SEM DESCONTO! Valor final: R${:.2f}'.format(p))
else:
    print('20% de juros! Valor final: R${:.2f}'.format(p*1.20))
