from random import randint
from time import sleep
lista = []


def sorteia():
    print('Sorteando 5 numeros da lista: ', end='')
    for s in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[s], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    x = 0
    for c in lista:
        if c % 2 == 0:
            x += c
    print(f'Somando os valores pares de {lista}, temos {x}')


sorteia()
somaPar()
