from random import randint
from time import sleep
print('=-'*25)
print(f'{"jogo da megasena":^50}')
print('=-'*25)
quantos = int(input('quantos jogos voce quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {quantos} JOGOS', '-='*3)
temp = list()
lquantos = list()
for c in range(0, quantos):
    pos = 0
    while pos != 6:
        n = randint(0, 60)
        if n not in temp:
            temp.append(n)
            pos += 1
    temp.sort()
    lquantos.append(temp[:])
    temp.clear()
for c, v in enumerate(lquantos):
    print(f'jogo {c+1}: {v}')
    sleep(1)
print(f'{" cabo ":-^50}')
