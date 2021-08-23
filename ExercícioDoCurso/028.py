import random
import time
import sys
print("\033[1;35m_-=-_" * 10)
print("De 0 a 5 qual número você acha que eu pensei?")
print("_-=-_" * 10)
op = int(input("\033[1;33mTente adivinhar: "))
pc = random.randint(0, 5)

def animate():
 print("\033[1;35m-=-" * 3)
 sys.stdout.write('\r\033[1;32mPensando')
 time.sleep(0.3)
 sys.stdout.write('\rPensando.')
 time.sleep(0.3)
 sys.stdout.write('\rPensando..')
 time.sleep(0.3)
 sys.stdout.write('\rPensando...')
 time.sleep(0.3)
 sys.stdout.write('\rPensando')
 time.sleep(0.3)
 sys.stdout.write('\rPensando.')
 time.sleep(0.3)
 sys.stdout.write('\rPensando..')
 time.sleep(0.3)
 sys.stdout.write('\rPensando...')
 time.sleep(0.3)
 sys.stdout.write('\rPensando \n')
 time.sleep(0.3)
 print("\033[1;35m-=-" * 7)
animate()
if op > 5:
    print("Coloque um número menor ou igual a 5")
else:
    if op == pc:
        print("\033[1;32mPARABÉN VOCÊ ACERTOU \n\033[1;35m-=--=--=--=--=--=--=-\033[1;32m \nNúmero \033[1;35m{}".format(pc))
    else:
        print("\033[1;31mVocê Errou :( \nO número Que Eu pensei era \033[1;31;107m{}\033[m \n\033[1;31mE o seu \033[1;31;107m{}\033[m".format(pc, op))
