cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
n = int(input('digite um numero: '))
r = n % 2
if r == 1:
    print(cor['azul'], 'o numero {} é IMPAR'.format(n))
else:
    print(cor['azul'], 'o numero {} é PAR'.format(n))
