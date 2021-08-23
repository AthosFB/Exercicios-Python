gols = list()
dados = dict()
jogadores = list()
cont = " "
totgols = 0
while True:
    dados["Nome"] = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))
    for p in range(1, partidas + 1):
        g = int(input(f" -Quantos gols {dados['Nome']} fez na {p}º partida: "))
        gols.append(g)
        totgols += g
    dados["Gols"] = gols[:]
    dados["Total"] = totgols
    jogadores.append(dados.copy())
    while cont not in "SN":
        cont = str(input("Deseja continuar (S/N): ")).strip().upper()[0]
    if cont == "N":
        break
    gols.clear()
    totgols = 0
    cont = " "
    print("-=" * 30)
print("-=" * 30)
print("Nº   ", end=" ")
for k in dados.keys():
    print(f"{k:<10}", end=" ")
print()
print("-" * 40)
for enu, c in enumerate(jogadores):
    print(f"{enu}    ", end=" ")
    for v in c.values():
        print(f"{str(v):<15}", end=" ")
    print()
print("-" * 40)
while True:
    qual = int(input("Qual Jogador deseja ver (999 para parar): "))
    if qual == 999:
        break
    while qual >= len(jogadores) or qual < 0:
        print("Valor incorreto!!!")
        qual = int(input("Qual Jogador deseja ver (999 para parar): "))
    print(f"--- Sobre o jogador {jogadores[qual]['Nome']} ---")
    for num, gol in enumerate(jogadores[qual]["Gols"]):
        print(f"  -No {num + 1}º jogo ele fez {gol} gols.")
    print(f"Ao todo {jogadores[qual]['Total']} gols")
    print("-=" * 30)
print("-=" * 30)
print("  <<< PROGRAMA FINALIZADO >>>")
