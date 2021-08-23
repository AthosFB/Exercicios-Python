import math
n = float(input('Coloque um número: '))
A = math.trunc(n)
B = n - A
R = math.sqrt(n)
print('O número inteiro é {}, e a parte fracionada é {:.2f}. E a raiz quadrada dele é {:.2f}'.format(A, B, R))
