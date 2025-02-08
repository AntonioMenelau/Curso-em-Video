from math import ceil, floor
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
n = float(input('digite um numero com virgula:'))
int1 = floor(n)
int2 = ceil(n)
print('o numero {}{}{} é aproximadamente {}{}{} e {}{}{}'
      .format(cor['verde'], n, cor['l'],
              cor['azul'], int1, cor['l'],
              cor['azul'], int2, cor['l']))
