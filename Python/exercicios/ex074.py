from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print('os valores sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\no maior numero foi: {max(n)}')
print(f'o menor numero foi: {min(n)}')
