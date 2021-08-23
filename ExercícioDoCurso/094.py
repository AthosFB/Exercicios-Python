tempo = dict()
pessoas = list()
tempo["nome"] = " "
tempo["sexo"] = " "
cont = " "
while True:
    tempo["nome"] = str(input("Nome: "))
    tempo["idade"] = int(input("Idade: "))
    while tempo["sexo"] not in "MF":
        tempo["sexo"] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if tempo["sexo"] in "MF":
            break
        print("ERRO. Respostas apenas [M/F]")
    while cont not in "SN":
        cont = str(input("Continuar: [S/N] ")).strip().upper()[0]
        if cont in "SN":
            break
        print("ERRO. Respostas apenas [S/N]")
    if cont == "N":
        pessoas.append(tempo.copy())
        tempo.clear()
        break
    pessoas.append(tempo.copy())
    tempo["nome"] = " "
    tempo["sexo"] = " "
    cont = " "
    print("-=" * 20)
mi = 0
for enu, c in enumerate(pessoas):
    mi += pessoas[enu]["idade"]
mif = mi / (enu + 1)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
print(f"B) A média de idade é {mif:.2f} anos.")
print("C) As Mulheres cadastradas são: ", end=" ")
for conjun in pessoas:
    if conjun["sexo"] == "F":
        print(conjun["nome"], end="... ")
print(f"\nD) Pessoas acima da média de idade:")
for con in pessoas:
    if con["idade"] > mif:
        for key, item in con.items():
            print(f"{key} = {item}; ", end="")
        print()
print("-=" * 20)
print("     === PROGRAMA ENCERRADO ===")
print("-=" * 20)
