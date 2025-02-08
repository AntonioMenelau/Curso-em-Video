def aumentar(x=0, porc=0, form=False):
    resp = x * (1 + porc / 100)
    return moeda(resp) if form else resp


def diminuir(x=0, porc=0, form=False):
    resp = x * (1 - porc / 100)
    return moeda(resp) if form else resp


def dobro(x=0, form=False):
    resp = 2 * x
    return moeda(resp) if form else resp


def metade(x=0, form=False):
    resp = x / 2
    return moeda(resp) if form else resp


def moeda(x=0, moed='R$'):
    return f'{moed}{x:.2f}'.replace('.', ',')
