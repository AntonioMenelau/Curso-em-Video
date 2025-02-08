print('~'*60)
print(f'{"leitor de numeros":^60}')
print('~'*60)
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'digite um numero para a posiçao {c}: ')))
maior = max(lista)
menor = min(lista)
print('-=-'*20)
print(f'Voce digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
pos = 0
for c in lista:
    if c == maior:
        print(lista.index(maior, pos), end='...')
    pos += 1
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
pos = 0
for c in lista:
    if c == menor:
        print(lista.index(menor, pos), end='...')
    pos += 1
