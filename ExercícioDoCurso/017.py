import math
n = float(input('Coloque um cateto: '))
n2 = float(input('Coloque o outro cateto: '))
hipo = math.hypot(n, n2)
print('A ipotenusa de {} e {} é {:.2f}'.format(n, n2, hipo))