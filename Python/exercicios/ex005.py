n = int(input('digite um numero:'))
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
sus = n+1
ant = n-1
print('seu sucessor é {}{}{} e seu antecessor é {}{}{}'
      .format(cor['amarelo'], sus, cor['l'],
              cor['azul'], ant, cor['l']))
