lista = list()
for c in range(0, 5):
    lista.append(int(input(f"Coloque o valor número {c}º: ")))
mai = max(lista)
men = min(lista)
cont = 0
print("&&" * 25)
print(f"Você digitou os números: {lista}")
print(f"O menor valor é o {men}, que esta nas posições: ", end="")
while cont != 5:
    if lista[cont] == men:
        print(cont, end="... ")
    cont += 1
cont = 0
print(f"\nO maior valor é o {mai}, que esta nas posições: ", end="")
while cont != 5:
    if lista[cont] == mai:
        print(cont, end="... ")
    cont += 1
print()
print("&&" * 25)
