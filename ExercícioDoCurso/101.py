def voto():
    from datetime import date
    ano = int(input("Em que ano Você nasceu: "))
    print("\033[1;35mO seu voto é: \033[m")
    idade = date.today().year - ano
    if idade < 16:
        print(f"Idade {idade}: \033[1;31mVoto Negado\033[m")
    elif 15 < idade < 18 or idade >= 70:
        print(f"Idade {idade}: \033[1;33mVoto Opicional\033[m")
    else:
        print(f"Idade {idade}: \033[1;32mVoto Obrigatório\033[m")


voto()
