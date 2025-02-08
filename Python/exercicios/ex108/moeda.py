def aumentar(x=0, porc=0):
    resp = x * (1 + porc / 100)
    return resp


def diminuir(x=0, porc=0):
    resp = x * (1 - porc / 100)
    return resp


def dobro(x=0):
    resp = 2 * x
    return resp


def metade(x=0):
    resp = x / 2
    return resp


def moeda(x=0, moed='R$'):
    return f'{moed}{x:.2f}'.replace('.', ',')
