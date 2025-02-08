cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
adj = float(input('digite o cateto {}adjacente{}:'
                  .format(cor['vermelho'], cor['l'])))
opo = float(input('digite o cateto {}oposto{}:'
                  .format(cor['vermelho'], cor['l'])))
hip = (adj**2 + opo**2)**(1/2)
print('a hipotenusa é {}{:.2f}{}'
      .format(cor['azul'], hip, cor['l']))
