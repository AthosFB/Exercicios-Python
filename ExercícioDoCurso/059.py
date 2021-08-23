from time import sleep
print("\033[1;33m-=-" * 10)
n1 = float(input("\033[1;97mColoque o 1º Valor: "))
print("\033[1;33m-=-" * 10)
n2 = float(input("\033[1;97mColoque o 2º Valor: "))
print("\033[1;33m-=-" * 10)
op = 0
while op != 5:
    print("\033[1;33m-=-" * 10)
    print("\033[1;97m[ 1 ] Para Somar")
    print("\033[1;33m-=-" * 10)
    print("\033[1;97m[ 2 ] Para Multiplicar")
    print("\033[1;33m-=-" * 10)
    print("\033[1;97m[ 3 ] Para Achar o Maior")
    print("\033[1;33m-=-" * 10)
    print("\033[1;97m[ 4 ] Para Trocar os Números")
    print("\033[1;33m-=-" * 10)
    print("\033[1;97m[ 5 ] Para Sair do programa")
    print("\033[1;33m-=-" * 10)
    op = int(input("Sua opção: "))
    print("\033[1;33m-=-" * 10)
    if op == 1:
        print("\033[1;32mA soma Entre {} + {} = {}".format(n1, n2, n1 + n2))
        print("\033[1;33m-=-" * 10)
    elif op == 2:
        print("\033[1;32mA multiplicação entre {} * {} = {}".format(n1, n2, n1 * n2))
        print("\033[1;33m-=-" * 10)
    elif op == 3:
        if n1 > n2:
            print("\033[1;32mA 1º opção é maior {}".format(n1))
            print("\033[1;33m-=-" * 10)
        elif n2 > n1:
            print("\033[1;32mA 2º opção é maior {}".format(n2))
            print("\033[1;33m-=-" * 10)
        else:
            print("\033[1;32mAs duas são iguais")
            print("\033[1;33m-=-" * 10)
    if op == 4:
        n1 = float(input("Coloque o 1º Valor: "))
        print("\033[1;33m-=-" * 10)
        n2 = float(input("Coloque o 2º Valor: "))
        print("\033[1;33m-=-" * 10)
    if op == 5:
        print("Finalizando...")
        sleep(2)
        break
