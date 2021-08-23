tempo = list()
princ = list()
import random
import time
import sys
print("-=" * 20)
print(f"{'MEGA SENA': ^40}")
print("-=" * 20)
quant = int(input("Quantos jogos deseja jogar? "))
cont = 0
while cont != quant:
    for n in range(0, 6):
        a = random.randint(1, 60)
        while a in tempo:
            a = random.randint(1, 60)
        tempo.append(a)
    princ.append(tempo[:])
    tempo.clear()
    cont += 1
for s in range(0, quant):
    princ[s].sort()
for enu, con in enumerate(princ):
    print("\033[m-=" * 20)
    print(f"\033[mO {enu + 1}º jogo {con}")
    def animation():
        sys.stdout.write(f"\r\033[1;32m{enu + 1}º Jogo carregado!!!\n")
        time.sleep(0.5)
    animation()
    time.sleep(0.5)
print(f"\033[m{' BOA SORTE ':=^40}")
