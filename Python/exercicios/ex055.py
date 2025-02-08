print('-=-'*20)
print(' '*15, '\033[35manalisador de peso\033[m')
print('-=-'*20)
maior = 0
menor = 0
for c in range(1, 6, 1):
    peso = float(input('peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso é {:.1f}Kg'.format(maior))
print('o menor peso é {:.1f}Kg'.format(menor))
