aluno = dict()
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))
if 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
elif aluno["Média"] < 5:
    aluno["Situacao"] = "Reprovado"
else:
    aluno["Situacao"] = "Aprovado"
print("-=" * 15)
for k, i in aluno.items():
    print(f"{k} recebe {i}")
print("-=" * 15)
print("<<<PROGRAMA FINALIZADO>>>")
