def jogou(jog="<desconhecido>", gol=0):
    print(f"O jogador {jog} fez {gol} gol(s)")


a = str(input("Nome do Jogador: "))
if a == "" or a == " ":
    a = "<desconhecido>"
b = str(input("Número de gols: "))
if b.isdigit() == False:
    b = 0
jogou(a, b)
