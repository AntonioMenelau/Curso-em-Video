n = int(input('digite um numero:'))
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
dob = n*2
tri = n*3
rai = n**(1/2)
print('o dobro do seu numero é {}{:.2f}{}'
      .format(cor['lilas'], dob, cor['l']))
print('o triplo do seu numero é {}{:.2f}{}'
      .format(cor['cinza'], tri, cor['l']))
print('a raiz do seu numero é {}{:.2f}{}'
      .format(cor['vermelho'], rai, cor['l']))
