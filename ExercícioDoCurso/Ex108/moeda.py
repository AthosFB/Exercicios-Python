def dobro(n):
    tot = n * 2
    return tot


def metade(n):
    tot = n / 2
    return tot


def aumentar(n, taxa):
    c = 100 + taxa
    tot = (n / 100) * c
    return tot


def diminuir(n, taxa):
    c = 100 - taxa
    tot = (n / 100) * c
    return tot


def moeda(num, moeda="R$"):
    n = f"{moeda}{num:.2f}"
    c = n.replace(".", ",")
    return c
