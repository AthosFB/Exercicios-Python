n = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
     "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte", "controle")
op = -1
while True:
    while op > 20 or op < 0:
        print("---" * 5)
        op = int(input("Escolha um número entre 0 e 20: "))
    print("---" * 5)
    print(n[op])
    op = -1
    cont = " "
    while cont not in "SN":
        print("---" * 5)
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
print()
print("\033[1;31mPROGRAMA FINALIZADO")
