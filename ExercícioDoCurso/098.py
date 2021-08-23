from time import sleep


def cont(a, b, c):
    if c == 0:
        c = 1
    elif c < 0:
        c = (c - c - c)
    print("\033[1;33m-=\033[m" * 20)
    print(f"Contagem de {a} até {b} pulando de {c} em {c}")
    if a < b and c > 0:
        for i in range(a, b + 1, c):
            print(f"\033[1;35m{i}", end=" ")
            sleep(0.5)
    elif a > b and c > 0:
        c = c - (c + c)
        for i in range(a, b - 1, c):
            if i >= b:
                print(f"\033[1;35m{i}", end=" ")
            sleep(0.5)
    print("Fim!")
    sleep(1)
    print("\033[1;33m-=\033[m" * 20)


cont(1, 10, 1)
print()
cont(10, 0, 2)
print(" -Agora é sua vez!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Pula: "))
cont(i, f, p)
