import random
chute = 99
pc = random.randint(0, 10)
c = 0
while pc != chute:
    print("\033[1;33m-=-" * 10)
    print("\033[1;33mDe 0 a 10. Em qual número estou pensando?")
    chute = int(input("\033[1;35mTente Adivinhar: "))
    c += 1
    if pc > chute:
        print("\033[1;33m-=-" * 10)
        print("\033[1;97mUm pouco Mais!")
    elif pc == chute:
        print("\033[1;33m-=-" * 10)
        print("\033[1;32mBoa!!!")
    else:
        print("\033[1;33m-=-" * 10)
        print("\033[1;97mUm pouco Menos!")
print("\033[1;33m-=-" * 10)
print("\033[1;32mPARABÉNS!!! Você me venceu!")
print("\033[1;97mVocê precisou de \033[1;31m{} \033[1;97mpalpites para ganhar!".format(c))
