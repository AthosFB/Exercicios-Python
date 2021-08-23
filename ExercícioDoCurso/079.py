lista = list()
cont = " "
while True:
    n = int(input("Coloque um número: "))
    if n in lista:
        print("\033[1;31mNúmero já existente na lista, ele não foi adicionado!\033[m")
    else:
        print("\033[1;32mNúmero adicionado a sua lista!\033[m")
        lista.append(n)
    while cont not in "SN":
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
print("A sua lista foi ", end="")
for c in sorted(lista):
    print(c, end="... ")
    