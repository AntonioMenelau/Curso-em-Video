cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
salario = int(input('qual é o salario do funcionario? '))
if salario > 1200:
    total = salario * 1.1
else:
    total = salario * 1.15
print('parabens, voce agora recebe {}R${:.2f}{}'
      .format(cor['azul'], total, cor['l']))
