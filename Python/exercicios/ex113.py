def leiaint():
    while True:
        try:
            x = int(input('Digite um numero inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um numero inteiro válido.\033[m')
            continue
        except InterruptedError:
            print('\033[31mO usiario decidiu não definir um valor\033[m')
            return 0
        else:
            return x


def leiafloat():
    while True:
        try:
            x = float(input('Digite um numero real: '))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um numero real válido.\033[m')
            continue
        except InterruptedError:
            print('\033[31mO usiario decidiu não definir um valor\033[m')
            return 0
        else:
            return x


numint = leiaint()
numreal = leiafloat()
print(f'O numero Real é {numreal} e o numero inteiro é {numint}')
