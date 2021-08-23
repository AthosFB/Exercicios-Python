lista = [[], [], []]
cont = pt1 = pt2 = 0
for c in range(0, 9):
    if 3 <= c <= 5:
        cont = 1
    elif c >= 5:
        cont = 2
    lista[cont].append(int(input(f"Valor para [{pt2}, {pt1}]: ")))
    if pt1 == 2:
        pt2 += 1
        pt1 = -1
    pt1 += 1
print("-=" * 10)
for la in lista:
    for m in la:
        print(f"[ {m:^5} ]", end="")
    print("\n", end="")
