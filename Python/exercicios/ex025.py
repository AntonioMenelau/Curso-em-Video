cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
name = str(input('qual o seu nome? ')).strip()
print('{}o seu nome tem Silva: {}'
      .format(cor['amarelo'], 'SILVA' in name.upper()))
