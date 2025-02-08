cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
nome = str(input('digite o seu nome completo:'))
print(cor['vermelho'], 'o seu nome em maiusculo é {}'.format(nome.upper()))
print(cor['azul'], 'o seu nome em miuscula é {}'.format(nome.lower()))
print(cor['amarelo'], 'o seu nome tem {} letras'.format(len(nome)))
print(cor['lilas'], 'o seu primeiro nome tem {} letras'.format(nome.find(' ')))
