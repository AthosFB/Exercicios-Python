def dobro(n, formatador):
    tot = n * 2
    if formatador is True:
        num = f"R${tot:.2f}"
        c = num.replace(".", ",")
        return c
    else:
        return tot


def metade(n, formatador):
    tot = n / 2
    if formatador is True:
        num = f"R${tot:.2f}"
        c = num.replace(".", ",")
        return c
    else:
        return tot


def aumentar(n, taxa, formatador):
    c = 100 + taxa
    tot = (n / 100) * c
    if formatador is True:
        num = f"R${tot:.2f}"
        c = num.replace(".", ",")
        return c
    else:
        return tot


def diminuir(n, taxa, formatador):
    c = 100 - taxa
    tot = (n / 100) * c
    if formatador is True:
        num = f"R${tot:.2f}"
        c = num.replace(".", ",")
        return c
    else:
        return tot


def moeda(num):
    n = f"R${num:.2f}"
    c = n.replace(".", ",")
    return c


def resumo(valor, vlrdoaumento, vlrdareducao):
    """

    :param valor: Valor a ser alterado
    :param vlrdoaumento: procentagem do aumento
    :param vlrdareducao: porcentagem da redução
    :return:
    """
    print("-" * 30)
    print(f"{'Tabela De Preços':^30}")
    print("-" * 30)
    print(f"{'Preço analizado: '} \t{moeda(valor)}")
    print(f"{'Dobro do Preço: '} \t{dobro(valor, formatador=True)}")
    print(f"{'Metado do Preço: '} \t{metade(valor, formatador=True)}")
    print(f"{f'{vlrdoaumento}% de aumento: '} \t{aumentar(valor,vlrdoaumento, formatador=True)}")
    print(f"{f'{vlrdareducao}% de redução: '} \t{diminuir(valor,vlrdareducao, formatador=True)}")
    print("-" * 30)


