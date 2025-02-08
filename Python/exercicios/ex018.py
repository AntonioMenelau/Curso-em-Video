from math import radians, sin, cos, tan
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
ang = float(input('digite o algulo: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tang = tan(rad)
print('seno= {}{:.2f}{}\n'
      'cos= {}{:.2f}{}\n'
      'tang= {}{:.2f}{}'
      .format(cor['vermelho'], sen, cor['l'],
              cor['verde'], cos, cor['l'],
              cor['azul'], tang, cor['l']))
