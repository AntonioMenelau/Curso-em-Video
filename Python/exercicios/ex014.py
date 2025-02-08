cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
temp = float(input('qual é a temperatura em °C: '))
fare = temp*1.8+32
print('a temperatura de {}{} °C{} corresponde a {}{} °F{}'
      .format(cor['azul'], temp, cor['l'],
              cor['azul'], fare, cor['l']))
