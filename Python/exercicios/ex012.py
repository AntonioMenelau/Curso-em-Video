cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
valor = float(input('quanto custa este produto?'))
desc = valor-(valor*0.05)
print('com o desconto de {}5%{} fica {}{:.2f}{}'
      .format(cor['lilas'], cor['l'],
              cor['lilas'], desc, cor['l']))
