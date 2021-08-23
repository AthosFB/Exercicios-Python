def lin():
    print("---" * 10)


def area(a, b):
    lin()
    tot = a * b
    print(f"A área de \033[1;32m{a}\033[m * \033[1;32m{b}\033[m recebe \033[1;32m{tot}\033[mMts²")
    lin()


lin()
print(f"{'Tamanho De Terrenos':^30}")
lin()
lar = int(input("Coloque a largura da área: "))
lin()
c = int(input("Coloque o comprimento da área: "))
area(a=lar, b=c)
