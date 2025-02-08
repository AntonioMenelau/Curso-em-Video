cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
km = float(input('quantos quilometro voce {}rodou{} com o carro?'
                 .format(cor['vermelho'], cor['l'])))
dia = int(input('quantos dias voce {}ficou{} com o carro?'
                .format(cor['vermelho'], cor['l'])))
valor = km*0.15+dia*60
print('voce deve pagar {}R${:.2f}{}'
      .format(cor['verde'], valor, cor['l']))
