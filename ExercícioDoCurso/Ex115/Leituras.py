def intput(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            print("\033[1;31mO usuario preferiu não informar o valor!!!\033[m")
        except:
            print("\033[1;31mValor Inválido")
            print("Tente Novamente!!!\033[1;30;107m")
        else:
            break
    return a
