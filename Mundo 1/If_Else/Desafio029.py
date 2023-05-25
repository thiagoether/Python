v = int(input('Informe a velocidade do veiculo:'))
if v > 80:
    print('Você foi multado! e sua multa custa R${}'.format((v-80)*7))
else:
    print('')
