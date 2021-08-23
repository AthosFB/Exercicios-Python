import random
a = input('Coloque o 1º item: ')
b = input('Coloque o 2º item: ')
c = input('Coloque o 3º item: ')
d = input('Coloque o 4º item: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem será: ')
print('==={}==='.format(lista))

