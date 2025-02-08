def fatorial(num, show=False):
    """
    Calculo de Fatorial com opiçao de ver resolução
    :param num: Numero a ser fatorado
    :param show: Se vai aparecer ou não a resolução
    :return: NONE
    Criado por Antonio Menelau
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    if show:
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
    print(f'{fat}')


fatorial(10, show=True)
