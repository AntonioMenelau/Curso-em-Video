num = list()
for cont in range(0, 5):
    num.append(int(input('digite um numero: ')))
for p, c in enumerate(num):
    print(f'o numero {c} esta na {p+1}ª posiçao')
print('cheguei ao final da lista!')
