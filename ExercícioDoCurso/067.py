while True:
    print()
    tabuada = float(input("Qual número da tabuada deseja ver: (Qualquer número negativo para parar) "))
    print()
    cont = 1
    if tabuada < 0:
        break
    while cont != 11:
        print(f"{cont} * {tabuada} = {cont * tabuada:.2f}")
        cont += 1
print("Fim")
