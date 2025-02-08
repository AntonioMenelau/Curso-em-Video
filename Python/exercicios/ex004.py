n = input('digite algo:')
cor = {'limpo':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
print('ele é numero? {}{}{}'.format(cor['verde'], n.isnumeric(), cor['limpo']))
print('ele é uma letra? {}{}{}'.format(cor['amarelo'], n.isalpha(), cor['limpo']))
print('ele é maiuscula? {}{}{}'.format(cor['azul'], n.isupper(), cor['limpo']))
print('ele é minuscula? {}{}{}'.format(cor['vermelho'], n.islower(), cor['limpo']))
print('ele é alfanumerico? {}{}{}'.format(cor['lilas'], n.isalnum(), cor['limpo']))
print('ele é capitalizada? {}{}{}'.format(cor['cinza'], n.istitle(), cor['limpo']))
