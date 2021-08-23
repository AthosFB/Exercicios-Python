import random
import time
import sys
print("\033[1;35m-#-" * 6)
print("[ 1 ] Para Pedra")
print("[ 2 ] Para Papel")
print("[ 3 ] Para Tesoura")
op = int(input("\033[1;33mOpção Número: "))

pcop = random.choices(["pedra", "papel", "tesoura"])
print("\033[1;35m-#-" * 6)
def animaition():
    sys.stdout.write("\r\033[1;32mPensando")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>>")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>>>")
    time.sleep(0.2)
    sys.stdout.write("\rPensando")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>>")
    time.sleep(0.2)
    sys.stdout.write("\rPensando>>>")
    time.sleep(0.2)
    sys.stdout.write("\rVai esse Então")
    time.sleep(1)
    sys.stdout.write("\r \n\033[m")
    time.sleep(0.3)
animaition()
print("\033[1;35m-#-" * 6)
if op == 1 and pcop == ["pedra"]:
    print("\033[1;33mEmpate, Os 2 Escolheram Pedra.")
elif op == 1 and pcop == ["papel"]:
    print("\033[1;31mO computador Ganhou! Ele escolheu papel.")
elif op == 1 and pcop == ["tesoura"]:
    print("\033[1;32mVocê ganhou Ganhou! Ele escolheu tesoura.")

if op == 2 and pcop == ["pedra"]:
    print("\033[1;32mVocê Ganhou! O computador Escolheu pedra.")
elif op == 2 and pcop == ["papel"]:
    print("\033[1;33mEmpate, Os 2 Escolheram papel")
elif op == 2 and pcop == ["tesoura"]:
    print("\033[1;31mVocê perdeu! Ele escolheu tesoura.")

if op == 3 and pcop == ["pedra"]:
    print("\033[1;31mCê perdeu! O computador Escolheu pedra")
elif op == 3 and pcop == ["papel"]:
    print("\033[1;32mVocê Ganhou! Ele escolheu papel.")
elif op == 3 and pcop == ["tesoura"]:
    print("\033[1;33mE é Empaaate! Vocês escolheram tesoura.")
print("\033[1;35m-#-" * 6)