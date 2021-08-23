import math
n1 = float(input('Coloque o ângulo: '))
n = math.radians(n1)
seno = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)
print('O seno é {:.2f}'.format(seno))
print('O Cosseno é {:.2f}'.format(cos))
print('A tangente é {:.2f}'.format(tan))
