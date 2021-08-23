"""num = int(input("Coloque um número: "))
c = num
res = num
while c != 1 and num != 0:
    print(c, end="")
    print(" x " if c > 2 else " = ", end="")
    c -= 1
    res = res * c
print("A fatoração de 0 é Igual a 1" if num == 0 else "{}".format(res))"""

# OU

"""if num == 0:
    print("A fatoração de 0 é Igual a 1")
else:
    print("{}".format(res))"""

res = 0
n = int(input("Coloque Um número: "))
for c in range(1, n):
    n = c * n
print(1 if n == 0 else n)

