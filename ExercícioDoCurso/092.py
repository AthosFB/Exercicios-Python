import datetime
while True:
    trabalhador = {"Nome": str(input("Nome: ")),
                   "Idade": datetime.date.today().year - int(input("Ano de nascimento: ")),
                   "ctps": int(input("Carteira de trabalho: (0 não tem) "))}
    if trabalhador["ctps"] == 0:
        break
    else:
        trabalhador["Contratação"] = int(input("Em que ano foi contratado(a): "))
        trabalhador["Salario"] = float(input("Coloque seu salário: R$"))
        trabalhador["Aposentadoria"] = trabalhador["Contratação"] - trabalhador["Nascimento"] + 35
        break
print("-=" * 25)
for k, v in trabalhador.items():
    print(f"  -{k} tem o valor de {v}")
