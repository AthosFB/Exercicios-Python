tempo = list()
tot = 0
jogo = {"Jogador": str(input("Coloque o nome no jogador: "))}
part = int(input(f"Quantas partidas {jogo['Jogador']} jogou: "))
for j in range(0, part):
    tempo.append(int(input(f"  -Gols na partida {j + 1}: ")))
jogo["Gols"] = tempo
for g in jogo["Gols"]:
    tot += g
jogo["Total"] = tot
print("-=" * 25)
print(jogo)
print("-=" * 25)
for k, v in jogo.items():
    print(f"  -O campo {k} recebe {v}")
print("-=" * 25)
print(f"O jogador {jogo['Jogador']} jogou {part} partidas")
for enu, ite in enumerate(jogo["Gols"]):
    print(f"  =>Na {enu + 1}º partida {jogo['Jogador']} fez {ite} gols.")
print(f"Ao todo {jogo['Jogador']} fez {jogo['Total']} gols")
print("-=" * 25)
print("             == Volte Sempre ==")
print("-=" * 25)
