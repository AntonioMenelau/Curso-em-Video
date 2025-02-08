from time import sleep
from random import randint
from operator import itemgetter

dic = {'Jogador1': randint(1, 6),
       'Jogador2': randint(1, 6),
       'Jogador3': randint(1, 6),
       'Jogador4': randint(1, 6)}
ordem = list()
for i, v in dic.items():
    print(f' {i} tirou: {v}')
    sleep(0.5)

ordem = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == Ranking dos Jogadores ==')
for i, v in enumerate(ordem):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
