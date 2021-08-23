from Ex115 import meusql
from Ex113 import Leituras
from Ex115 import Escritas
meusql.db()
meusql.tabelas()
while True:
    Escritas.inicio()
    num = Leituras.intput("Escolha a opção: ")
    print("---" * 15)
    while num > 4:
        print("\033[1;31mERRO: NÚMERO INVÁLIDO!!!\033[1;30;107m")
        num = Leituras.intput("Escolha a opção: ")
        print("---" * 15)
        if num <= 4:
            break
    if num == 1:
        print("\033[1;30;107m---" * 15)
        print(f"{'Pessoas Cadastradas':^45}")
        print("---" * 15)
        meusql.escrever()
    elif num == 2:
        print("\033[1;30;107m---" * 15)
        print(f"{'Pessoas Cadastradas':^45}")
        print("---" * 15)
        meusql.escrever(idade=True)
    elif num == 3:
        meusql.add()
    elif num == 4:
        Escritas.saida()
        break
