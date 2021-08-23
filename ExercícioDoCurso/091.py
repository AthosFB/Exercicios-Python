import random
import time
from operator import itemgetter
jogo = {"jogador1": random.randint(1, 6),
        "jogador2": random.randint(1, 6),
        "jogador3": random.randint(1, 6),
        "jogador4": random.randint(1, 6)}
ranking = {}
print("Valore Sorteados: ")
for k, n in jogo.items():
    print(f"{k} recebe \033[1;32m{n}\033[m")
    time.sleep(1)
print("-=" * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("  === Ranking Dos Jogadores ===")
for enu, c in enumerate(ranking):
    print(f"  -{enu+1}º Lugar {c[0]} com \033[1;32m{c[1]}\033[m")
    time.sleep(1)
