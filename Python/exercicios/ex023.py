cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
n = int(input('digite um numero inteiro: '))
m = (n % 10000) // 1000
c = (n % 1000) // 100
d = (n % 100) // 10
u = (n % 10) // 1
print('unidade:{}{}{}\n'
      'dezena:{}{}{}\n'
      'centena:{}{}{}\n'
      'milhar:{}{}{}'
      .format(cor['vermelho'], u, cor['l'],
              cor['azul'], d, cor['l'],
              cor['amarelo'], c, cor['l'],
              cor['verde'], m, cor['l']))
