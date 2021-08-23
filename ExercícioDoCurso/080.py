lista = list()
for c in range(0, 5):
    num = int(input("Coloque um número: "))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        lc = 0
        while lc < len(lista):
            if num <= lista[lc]:
                lista.insert(lc, num)
                break
            lc += 1
print(lista)

