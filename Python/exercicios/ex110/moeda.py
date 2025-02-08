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


def resumo(x=0, pora=10, pord=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f"preço analisado: \t{moeda(x)}")
    print(f"dobro do preço: \t{dobro(x, True)}")
    print(f"metade do preço: \t{metade(x, True)}")
    print(f"{pora} % de aumento: \t{aumentar(x, 20, True)}")
    print(f"{pord} % de redução: \t{diminuir(x, 12, True)}")
    print('-'*30)
