casa = int(input("Quanto Vai custar a casa? "))
salario = int(input("Qual é o seu salario? "))
anos = int(input("Em quantos anos pretende pagar? "))

saldispo = (salario / 10) * 3
mes = anos * 12
confirm = (casa / mes) - saldispo
parcela = casa / mes
falta = parcela - saldispo

if confirm <= 0:
    print("\033[1;32mVocê pode pagar essa casa!\033[m")
    print("Você gastara \033[1;32mR${:.2f}\033[m por mês".format(parcela))

else:
    print("\033[1;31mVocê não pode pagas essa casa!\033[m")
    print("Faltará \033[1;31mR${:.2f}\033[m por mês".format(falta))
