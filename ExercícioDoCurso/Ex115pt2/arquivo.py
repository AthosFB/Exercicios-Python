def arquivoExiste(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq):
    try:
        a = open(arq, "wt+")
        a.close()
    except:
        print("Ouve um erro na criação do arquivo!!!")
    else:
        print("Arquivo criado com sucesso!!!")


def escrever(arq, nome, idade):
    try:
        a = open(arq, "at")
    except:
        print("Erro!!!")
    else:
        try:
            a.write(f"{nome};{idade}")
            a.write("\n")
        except:
            print("Ocorreu um erro")
        else:
            print(f"{nome} cadastrado(a) com sucesso")
            a.close()


def ler(arq):
    try:
        a = open(arq, "rt")
    except:
        print("Erro ao ler o arquivo!!!")
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<20}{dado[1]:>5}")
