valo = [int(input("Coloque o valor número 0: ")),
        int(input("Coloque o valor número 1: ")),
        int(input("Coloque o valor número 2: ")),
        int(input("Coloque o valor número 3: ")),
        int(input("Coloque o valor número 4: "))]
print("-==-" * 10)
print(f"Você digitou os valores {valo}")
a = valo.index(min(valo))
count = a + 1
b = valo.index(max(valo))
count2 = b + 1
print(f"O menor valor digitado foi o {min(valo)}, que aparece nas posições: ", end="")
print(a, end="... ")
while count < 5:
    if valo[count] == min(valo):
        print(count, end="... ")
    count += 1
print(f"\nO maior valor digitado foi o {max(valo)}, que aparece nas posições: ", end="")
print(b, end="... ")
while count2 < 5:
    if valo[count2] == max(valo):
        print(count2, end="... ")
    count2 += 1
