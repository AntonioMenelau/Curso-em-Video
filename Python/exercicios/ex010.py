cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
reais = float(input('{}digite quantos reais voce tem: {}'
                    .format(cor['verde'], cor['l'])))
dolar = reais/5.22
print('voce tem {}{:.2f}{} dolar'
      .format(cor['lilas'], dolar, cor['l']))
