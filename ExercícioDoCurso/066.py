cont = soma = 0
while True:
    n = int(input("Coloque um número: "))
    if n == 999:
        break
    soma += n
    cont += 1
print()
print(f"A soma De {cont} valores Foi {soma}!")
