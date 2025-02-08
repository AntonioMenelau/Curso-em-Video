cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
lar = float(input('digite a largura da sua parede:'))
alt = float(input('digite a altura da sa parede:'))
area = lar*alt
tinta = area/2
print('a area da sua parede é {}{:.2f}{} metros quadrados\n'
      'e a quantidade de potes de tinta é {}{:.2f}{} potes'
      .format(cor['azul'], area, cor['l'],
              cor['amarelo'], tinta, cor['l']))
