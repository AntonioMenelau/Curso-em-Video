m = float(input('digite o numero em metros:'))
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
cet = m*100
mili = m*1000
print('em centimetros= {}{:.0f}{}\n'
      'em milimetros= {}{:.0f}{}'
      .format(cor['azul'], cet, cor['l'],
              cor['vermelho'], mili, cor['l']))
