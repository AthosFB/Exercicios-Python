t1 = float(input("Coloque o 1º Termo: "))
rz = float(input("Coloque A Razão: "))
c = 10
r = t1
print("===" * 35)
while c != 0:
    print(r, end=" ")
    print(" > " if c != 1 else ">>>", end=" ")
    r = r + rz
    c -= 1
print("Acabou")
print("===" * 35)
