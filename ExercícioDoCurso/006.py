n = float(input('\033[1;31;107mColoque o número:\033[m '))
d = n * 2
t = n * 3
rq = n ** (1/2)
rc = n ** (1/3)
print('O número: \033[36m{}\033[m\nO dobro: \033[36m{}\033[m\nO triplo: \033[36m{}\033[m\nA raiz quadrada: \033[36m{:.2f}\033[m\nE a Raiz Cubica: \033[36m{:.2f}'.format(n, d, t, rq, rc))
