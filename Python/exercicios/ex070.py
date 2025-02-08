titulo = '\033[31mcarrinho de compra\033[m'
print('-=-'*20)
print(f'{titulo:^60}')
print('-=-'*20)
total = mais = barato = produto = 0
nomebarato = ''
while True:
    nome = str(input('digite o nome do produto: ')).strip()
    custo = float(input('digite o custo do produto: '))
    stop = str(input('voce quer adicionar'
                     ' mais alguma outra cois no carrinho?'
                     ' [s/n]')).strip().lower()
    total += custo
    produto += 1
    if custo > 1000:
        mais += 1
    if produto == 1 or custo < barato:
        barato = custo
        nomebarato = nome
    if stop == 'n':
        break
print('{:-^60}'.format(' FINAL DA COMPRA '))
print(f'o total gasto é R${total:.2f}')
print(f'quantidade de produtos com valor acima de R$1000.00: {mais}')
print(f'nome do produto mais barato: {nomebarato}')
