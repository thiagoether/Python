d = int(input('Informe a distancia da viagem:'))
if d > 200:
    print('Valor da viagem: R${}'.format(d * 0.50))
else:
    print('Valor da viagem: R${}'.format(d * 0.45))