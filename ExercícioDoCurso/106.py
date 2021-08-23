def ajuda():
    from time import sleep
    while True:
        print("\033[1;97;102m---" * 10)
        print(f"{'Sistema de Ajuda PyHELP':^30}")
        print("---" * 10)
        print("\033[m", end="")
        pala = str(input("\033[1;97;40mFunção ou Biblioteca > "))
        if pala in "quitQuit(quit)(Quit)":
            print("\033[1;97;46m---" * 15)
            print(f"{'<<< SAINDO >>>':^45}")
            print("---" * 15)
            sleep(2)
            break
        print("\033[1;97;46m---" * 15)
        print(f"{'Acessando o Material de Apoio':>33}", pala)
        print("---" * 15)
        sleep(1.5)
        print("\033[m", end="")
        print("\033[1;30;107m", end="")
        help(pala)
        print("\033[m", end="")
        print("\033[1;97;102m---" * 10)
        print(f"{' < Comando (quit) Para Sair >':^30}")
        print("---" * 10)
        print("\033[m", end="")


ajuda()
