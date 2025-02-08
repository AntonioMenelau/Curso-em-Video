print('-=-'*20)
print(f'{"validador de numero":^60}')
print('-=-'*20)
lista = list()
while True:
    n = int(input('digite um numero: '))
    if n in lista:
        print('numero duplicado, falha ao adicionar na lista.')
    else:
        print('numero adicionado com sucesso.')
        lista.append(n)
    resp = str(input('voce quer adicionar mais algum numero?[s/n]')).strip()[0]
    if resp in 'nN':
        break
print('-=-'*20)
lista.sort()
print(f'os valores adicionado foram {lista}')
