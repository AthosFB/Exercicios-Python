altura = float(input('Coloque a altura da paredede em metros: '))
largura = float(input('Coloque a largura da parede em metros: '))
area = largura * altura
tinta = area / 11
print('A área da parede é {}m² \nE você vai precisar de {:.3f}L de tinta.'.format(area, tinta))
