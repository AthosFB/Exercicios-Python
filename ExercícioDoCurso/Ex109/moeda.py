def dobro(n, formatador):
    tot = n * 2
    if formatador is True:
        return moeda(tot)
    else:
        return tot


def metade(n, formatador):
    tot = n / 2
    if formatador is True:
        return moeda(tot)
    else:
        return tot


def aumentar(n, taxa, formatador):
    c = 100 + taxa
    tot = (n / 100) * c
    if formatador is True:
        return moeda(tot)
    else:
        return tot


def diminuir(n, taxa, formatador):
    c = 100 - taxa
    tot = (n / 100) * c
    if formatador is True:
        return moeda(tot)
    else:
        return tot


def moeda(num, moeda="R$"):
    n = f"{moeda}{num:.2f}"
    c = n.replace(".", ",")
    return c
