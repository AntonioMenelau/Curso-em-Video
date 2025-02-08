temp = []
prin = []
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(int(input('peso: ')))
    if len(prin) == 0:
        maior = menor = temp[1]
    elif temp[1] > maior:
        maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [s/n] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'ao todo voce cadastrou {len(prin)} pessoas')
print(f'o maior peso foi {maior}Kg. Peso de ', end='')
for c in prin:
    if c[1] == maior:
        print(c[0], end='')
print()
print(f'o menor peso foi {menor}Kg. Peso de ', end='')
for c in prin:
    if c[1] == menor:
        print(c[0], end=' ')
print()
