cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
coisa = str(input('{}digite o alguma coisa: '.format(cor['azul'])))
coisa = coisa.lower()+coisa.strip()
print('quantas vezes aparece a letra A? {}'
      .format(frase.count('a')))
print('em que posiçao ela aparece primeiro? {}'
      .format(frase.find('a')+1))
print('em que posiçao ela aparece por ultimo? {}'
      .format(frase.rfind('a')+1))
