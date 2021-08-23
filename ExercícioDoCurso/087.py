lista = [[], [], []]
cont = p1 = p2 = maior = sdp = 0
for c in range(0, 9):
    if 3 <= c <= 5:
        cont = 1
    elif c > 5:
        cont = 2
    lista[cont].append(int(input(f"Coloque na posição [{p1}, {p2}]: ")))
    if p2 >= 2:
        p2 = -1
        p1 += 1
    p2 += 1
print("-=" * 12)
for con in lista:
    for iten in con:
        print(f"[{iten:^5}]", end="")
    print()
for a in lista:
    for b in a:
        if b % 2 == 0:
            sdp += b
print("-=" * 12)
print(f"A soma dos valores pares é: {sdp}")
stc = lista[0][2] + lista[1][2] + lista[2][2]
print(f"A soma dos valores da 3º coluna resultam: {stc}")
cont = 0
while cont != 3:
    if cont == 0 or lista[1][cont] > maior:
        maior = lista[1][cont]
    cont += 1
print(f"O maior valor da 2º linha é o: {maior}")
