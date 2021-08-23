def fatorial(x, show=False):
    """
    _
     -> Calcula o Fatorial de Um número
    :param x: número do fatorial
    :param show: se for Falso Não mostra a resolução se for verdadeiro mostra a solução
    :return:
    """
    tot = 0
    cont = x
    cnt = x
    for c in range(1, x + 1):
        if c == 1:
            tot = cont
        else:
            tot = tot * cont
        cont -= 1
    if show == False:
        print("---" * 2)
        return tot
    else:
        print("---" * 20)
        for i in range(0, x):
            print(cnt, end="")
            if i != x - 1:
                print(" x", end=" ")
            else:
                print(" =", end=" ")
            cnt -= 1
        return tot


n = int(input("Coloque um número: "))
print(f"{fatorial(n, show=False)}")
