print("\033[1;97m-=-" * 10)
print("   10 - 1º Termos de Uma PA")
print("-=-" * 10)
r = 0
pt = int(input("1º Termo: "))
rz = int(input("Razão: "))
for c in range(pt, pt + (10 * rz), rz):
    print(c, end= " -> ")
print("Acabou")