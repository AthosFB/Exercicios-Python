def intput(x):
    import math
    while True:
        a = input(x)
        if a.isascii() is True and a.isnumeric() is False:
            print("\033[1;31mEsse valor não é um número (ou não é inteiro)!!!\033[m")
        else:
            b = float(a)
            z = math.trunc(b)
            if z - b == 0:
                break
            else:
                print("\033[1;31mEsse valor não é um número (ou não é inteiro)!!!\033[m")
    print()
    return a


n = intput(x="Coloque um Número inteiro (sem ponto ou vírgola): ")
print(f"Você digitou o valor {n}")
