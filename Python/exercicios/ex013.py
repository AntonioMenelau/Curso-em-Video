cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
sala = float(input('qual o seu salario?'))
aument = sala+(sala*0.15)
print('{}Parabens, agora seu salario virou R${:.2f}{}'
      .format(cor['amarelo'], aument, cor['l']))
