def notas(*n, sit=False):
    """
      -> Analiza as notas do aluno e da algumas informações
    :param n: Notas do Aluno
    :param sit: Se sit == True ele mostra a situação do aluno,
           ou se estiver em False ou não preenchida não mostra a situação do aluno
    :return: dicionário com todos os dados
    """
    info = dict()
    info["total"] = len(n)
    info["maior"] = max(n)
    info["menor"] = min(n)
    info["média"] = sum(n) / len(n)
    if sit is True:
        if info["média"] < 6:
            info["situação"] = "Ruim"
        elif 6 < info["média"] < 7.5:
            info["situação"] = "Razoável"
        else:
            info["situação"] = "Boa"
    return info


a = notas(5.5, 2.5, 10, 9, sit=True)
print(a)
