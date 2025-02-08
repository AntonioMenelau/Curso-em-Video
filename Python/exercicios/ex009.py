n = int(input('digite o numero:'))
t = {'n0': n*0,
     'n1': n*1,
     'n2': n*2,
     'n3': n*3,
     'n4': n*4,
     'n5': n*5,
     'n6': n*6,
     'n7': n*7,
     'n8': n*8,
     'n9': n*9,
     'n10': n*10}
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
print('tabuada do {}'.format(n))
print('{}*0= {}{}{}\n'
      '{}*1= {}{}{}\n'
      '{}*2= {}{}{}\n'
      '{}*3= {}{}{}\n'
      '{}*4= {}{}{}\n'
      '{}*5= {}{}{}\n'
      '{}*6= {}{}{}\n'
      '{}*7= {}{}{}\n'
      '{}*8= {}{}{}\n'
      '{}*9= {}{}{}\n'
      '{}*10= {}{}{}'
      .format(n, cor['verde'], t['n0'], cor['l'],
              n, cor['lilas'], t['n1'], cor['l'],
              n, cor['cinza'], t['n2'], cor['l'],
              n, cor['cinza'], t['n3'], cor['l'],
              n, cor['amarelo'], t['n4'], cor['l'],
              n, cor['verde'], t['n5'], cor['l'],
              n, cor['amarelo'], t['n6'], cor['l'],
              n, cor['azul'], t['n7'], cor['l'],
              n, cor['vermelho'], t['n8'], cor['l'],
              n, cor['azul'], t['n9'], cor['l'],
              n, cor['cinza'], t['n10'], cor['l']))
