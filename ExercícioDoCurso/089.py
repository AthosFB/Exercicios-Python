tempo = list()
alunos = list()
cont = " "
n = 0
while True:
    tempo.append(str(input("Nome: ")))
    tempo.append(float(input("Nota 1: ")))
    tempo.append(float(input("Nota 2: ")))
    alunos.append(tempo[:])
    tempo.clear()
    while cont not in "SN":
        cont = str(input("Continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
print("-=" * 20)
print("Nº | Nome        | Média")
print("__" * 20)
for enu, conjunto in enumerate(alunos):
    print(enu, end="    ")
    print(f"{conjunto[0]: <14}", end="")
    print(f"{(conjunto[1] + conjunto[2]) / 2:>3.2f}")
print("-=" * 20)
while True:
    n = int(input("Coloque o Nº Do aluno que deseja ver a nota: (999 para parar): "))
    if n == 999:
        break
    if n <= len(alunos) - 1:
        print("-=" * 20)
        print(f"As notas de {alunos[n][0]} são: [{alunos[n][1]}, {alunos[n][2]}]")
        print("-=" * 20)
print("-=" * 20)
print(f"{'Program Finalizado':^40}")
print("-=" * 20)
