from random import shuffle
from time import sleep
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
print(cor['vermelho'], '-=-'*20)
print(cor['azul'], '  '*7, 'embaralhador automatico')
print(cor['vermelho'], '-=-'*20, cor['l'])

n1 = str(input('digite a {}primeira{} pessoa: '
               .format(cor['verde'], cor['l'])))

n2 = str(input('digite a {}segunda{} pessoa: '
               .format(cor['vermelho'], cor['l'])))

n3 = str(input('digite a {}terceira{} pessoa: '
               .format(cor['azul'], cor['l'])))

n4 = str(input('digite a {}quarta{} pessoa: '
               .format(cor['amarelo'], cor['l'])))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('procesando ...')
sleep(3)
print(cor['amarelo'], lista, cor['l'])
