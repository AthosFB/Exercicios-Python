from random import randint
win = 0
while True:
    print("\033[1;33m=\033[m" * 20)
    op = " "
    while op not in "IiPp":
        op = str(input("Par ou Ímpar [I/P] ")).strip().upper()
    print("\033[1;33m=\033[m" * 20)
    n = int(input("Coloque seu número: "))
    pc = randint(0, 10)
    calc = pc + n
    if op == "I" and calc % 2 != 0:
        print("\033[1;33m=\033[m" * 20)
        print("\033[1;32mVocê Ganhou!!!\033[m")
        print(f"O computador escolheu {pc}")
        win += 1
    elif op == "P" and calc % 2 == 0:
        print("\033[1;33m=\033[m" * 20)
        print("\033[1;32mVocê Ganhou!!!\033[m")
        print(f"O computador escolheu {pc}")
        win += 1
    else:
        print("\033[1;33m=\033[m" * 20)
        print("\033[1;31mVocê perdeu!!!\033[m")
        print(f"O computador escolheu {pc}")
        print(f"Você ganhou \033[1;32m{win}\033[m partidas")
        print("\033[1;33m=\033[m" * 20)
        break
