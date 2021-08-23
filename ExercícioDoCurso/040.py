print("\033[1;33m-=-" * 7)
p1 = float(input("Nota da prova 1: "))
print("\033[1;33m-=-" * 7)
p2 = float(input("Nota da prova 2: "))
print("\033[1;33m-=-" * 7)
r = (p1 + p2) / 2
if r >= 6 and r <= 10:
    print("\033[1;32mVocê Passou!!!\033[m \nCom média {:.2f}".format(r))
elif r >= 5.75 and r < 6:
    print("\033[1;33mVocê passou no Limite!!!\033[m \nCom média {:.2f}".format(r))
elif r < 5.75:
    print("\033[1;31mVocê ficou de recuperação!!!\033[m \nCom média {:.2f}".format(r))