def saida():
    from time import sleep
    from sys import stdout
    stdout.write("\r   ")
    sleep(0.3)
    stdout.write("\r   <<<")
    sleep(0.3)
    stdout.write("\r   <<<   ")
    sleep(0.3)
    stdout.write("\r   <<<   Obrigado!")
    sleep(0.3)
    stdout.write("\r   <<<   Obrigado! Volte")
    sleep(0.3)
    stdout.write("\r   <<<   Obrigado! Volte Sempre.")
    sleep(0.3)
    stdout.write("\r   <<<   Obrigado! Volte Sempre.   >>>\n")
    sleep(0.3)
    print("---" * 15)


def inicio():
    print("\033[1;30;107m---" * 15)
    print(f"{'Menu Principal':^45}")
    print("---" * 15, end="")
    print("""
    \033[1;30;43m 1 - Ver Pessoas Cadastradas \033[1;30;107m
    \033[1;30;43m 2 - Ver Pessoas Por Idade   \033[1;30;107m
    \033[1;30;43m 3 - Adicionar novo Registro \033[1;30;107m
    \033[1;30;43m 4 - Sair do sistema         \033[1;30;107m""")
    print("---" * 15)
