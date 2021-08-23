lista = [[], []]
for c in range(0, 7):
    n = int(input("Coloque um número: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares digitados foram {lista[0]}")
print(f"Os valores impares digitados são {lista[1]}")
