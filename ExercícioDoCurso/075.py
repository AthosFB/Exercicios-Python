a = (int(input("Coloque um número: ")),
     int(input("Coloque mais um número: ")),
     int(input("Coloque outro número: ")),
     int(input("Coloque o último número: ")))
cont = totcont = 0
print("Os números que você digitou: ", end="")
for b in a:
    print(b, end=", ")
print("\nO valor 9 ", end="")
print(f"apareceu {a.count(9)} vez(es)"if 9 in a else "não apareceu na lista")
print(f"O valor 3 apareceu na {a.index(3) + 1}º opção." if 3 in a else "O número 3 Não aparece na lista.")
while cont < 4:
    if a[cont] % 2 == 0:
        totcont += 1
    cont += 1
print(f"Os valores par(es) apareceram {totcont} vez(es)")
