valor = int(input('\033[4;33mColoque um número: '))
ant = valor - 1
suce = valor + 1
print('\033[mO Antecessor é \033[1;35m{}\033[m e o sucessor é \033[1;31m{}\033[m'.format(ant, suce), end=' ')
print('E o valor original é \033[1;36m{}'.format(valor))