def leiaint(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um numero inteiro válido.\033[m')
            continue
        except InterruptedError:
            print('\033[31mO usuario decidiu não definir um valor\033[m')
            return 0
        else:
            return x


def linha(com=42):
    return "-" * com


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for opicao in lista:
        print(f'\033[33m{c}\033[m - \033[34m{opicao}\033[m')
        c += 1
    print(linha())
    opc = leiaint("Sua Opição: ")
    return opc
