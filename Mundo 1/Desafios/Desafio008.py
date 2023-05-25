met = int(input('Digite um valor em metros:'))
cent = met * 100
mili = met * 1000
km = met / 1000
hm = met / 100
dam = met / 10
dm = met * 10

print('A medida de {}m corresponde a:\nKilometro: {}\nHectometro: {}\nDecametro: {}\nDecimetro: {}\nCentimetro: {}\nMilimetro: {}'.format(met, km, hm, dam, dm, cent, mili))
