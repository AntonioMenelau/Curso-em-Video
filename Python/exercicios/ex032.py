from datetime import date
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
ano = int(input('digite o ano a ser analisado! digite 0 para verificar o ano em que voce esta: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}o ano {} é BISSEXTO'.format(cor['verde'], ano))
else:
    print('{}o ano {} não é BISSEXTO'.format(cor['amarelo'], ano))
