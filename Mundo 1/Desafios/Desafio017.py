import math
co = int(input('Cateto oposto:'))
ca = int(input('Cateto adjacente:'))
h = math.pow(co, 2) + math.pow(ca, 2) #calculo de forma matematica
print('Hipotenusa: {:.2f}'.format(math.sqrt(h)))
print('Hypot: {:.2f}'.format(math.hypot(co, ca))) #calculo usando a função do python
