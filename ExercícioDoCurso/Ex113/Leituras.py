def intput(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            print("\033[1;31mO usuario preferiu não informar o valor!!!\033[m")
        except (ValueError, TypeError):
            print("\033[1;31mValor Inválido")
            print("Tente Novamente!!!\033[m")
            continue
        else:
            break
    return a


def flotput(msg):
    while True:
        try:
            b = str(input(msg)).replace(",", ".")
            b = float(b)
        except KeyboardInterrupt:
            print("\033[1;31mO usuario preferiu não infor mar o valor!!!\033[m")
        except (ValueError, TypeError):
            print("\033[1;31mValor Inválido")
            print("Tente Novamente!!!\033[m")
            continue
        else:
            print("\033[1;32mValor Registrado\033[m")
            break
    return b
