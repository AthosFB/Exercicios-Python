def leiaDinheiro(frase):
    while True:
        contn = 0
        contp = 0
        valor = input(frase).replace(",", ".").strip()
        if valor in "":
            print(f"\033[1;31mValor '{valor}' inválido!!!\033[m")
        else:
            for c in valor:
                if c in "0123456789":
                    contn += 1
                elif c in ".":
                    contp += 1
            tot = contp + contn
            if tot == len(valor) and contp == 0 or contp == 1 and contn >= 1:
                n = float(valor)
                break
            else:
                print(f"\033[1;31mValor '{valor}' inválido!!!\033[m")
    return n


def leiaInteiro(x):
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