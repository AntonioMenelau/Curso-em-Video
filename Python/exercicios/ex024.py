cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
cit = str(input('em que cidade voce nasceu? '))
cit = cit.lower()+cit.strip()
print(cor['vermelho'], 'valinhos' in cit)
