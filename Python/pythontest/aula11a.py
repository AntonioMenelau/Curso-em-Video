m = str(input('digite algo: '))
cores = {'limpa': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'lilaz': '\033[35m',
        'azul bb': '\033[36m',
        'cinza': '\033[37m'}
print('\033[0;30;41m{}\033[m'.format(m))
print('\033[4;33;46m{}\033[m'.format(m))
print('\033[1;35;43m{}\033[m'.format(m))
print('\033[0;30;42m{}\033[m'.format(m))
print('\033[m{}\033[m'.format(m))
print('\033[7m{}\033[m'.format(m))
