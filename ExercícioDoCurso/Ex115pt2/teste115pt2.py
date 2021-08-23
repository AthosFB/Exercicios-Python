from Ex115pt2.arquivo import *
arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criararquivo(arq)
while True:
    print("---" * 30)
    print("1 - Ver Cadastrados")
    print("2 - Cadastrar")
    print("3 - Sair")
    print("---" * 30)
    op = int(input("Sua Opção: "))
    print("---" * 30)
    if op == 1:
        print(f"{'Nome':<20}{'Idade':>5}")
        print("---" * 30)
        ler(arq)
    elif op == 2:
        nome = str(input("Nome: "))
        print("---" * 30)
        idade = int(input("Idade: "))
        escrever(arq, nome, idade)
    elif op == 3:
        break
    else:
        continue
