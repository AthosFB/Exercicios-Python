direita = []
esquerda = []
cont = 0
esprecao = input("Coloque seua expreção numérica: ")
a = len(esprecao)
while cont != a:
    if esprecao[cont] == "(":
        esquerda.append(esprecao[cont])
    elif esprecao[cont] == ")":
        direita.append(esprecao[cont])
    cont += 1
    if len(direita) > len(esquerda):
        print("Espreção inválida!")
        break
if len(direita) == len(esquerda):
    print("Espreção válida")    
