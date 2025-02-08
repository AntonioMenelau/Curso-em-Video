from random import randint
from time import sleep
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
n1 = randint(0, 5)
print('-=-' * 20)
print(cor['azul'],'estou pensando em um numero entre 0-5:...tente adivinhar', cor['l'])
print('-=-' * 20)

n2 = int(input('digite o numero: '))   
print('PROCESSANDO...')
sleep(2)
if n2 == n1:
    print('parabens, voce acertou.')
else:
    print('oops, tente novamente.')
print('o numero era {}'.format(n1))
