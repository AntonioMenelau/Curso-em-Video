from random import choice
from time import sleep
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
n1 = str(input('{}o primeiro aluno: {}'
               .format(cor['vermelho'], cor['l'])))
n2 = str(input('{}o segundo aluno: {}'
               .format(cor['verde'], cor['l'])))
n3 = str(input('{}o terceiro aluno:{} '
               .format(cor['lilas'], cor['l'])))
n4 = str(input('{}o quarto aluno: {}'
               .format(cor['amarelo'], cor['l'])))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('processando ...')
sleep(3)
print('o escolhido é {}{}{}'
      .format(cor['azul'], escolhido, cor['l']))
