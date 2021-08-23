salario = float(input('Qual é o seu salario? R$'))
a = salario / 100 * 70
b = salario / 100 * 80
c = salario / 100 * 90
d = salario / 100 * 110
e = salario / 100 * 120
f = salario / 100 * 130
print()
print('_' * 20)
print('{} - 30% = {:.2f}'.format(salario, a))
print('{} - 20% = {:.2f}'.format(salario, b))
print('{} - 10% = {:.2f}'.format(salario, c))
print('{} - 5% = {:.2f}'.format(salario, salario / 100 * 95))
print('{} + 10% = {:.2f}'.format(salario, d))
print('{} + 20% = {:.2f}'.format(salario, e))
print('{} + 30% = {:.2f}'.format(salario, f))
print('_' * 20)
