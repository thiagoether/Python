l = float(input('Informe a largura da parede:'))
a = float(input('Informe a altura da parede:'))
area = l * a
tinta = area / 2
print('Área: {:.2f}m² \nQuantidade de tinta necessária: {:.2f}L'.format(area, tinta))