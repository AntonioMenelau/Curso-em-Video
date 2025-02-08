cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
km = float(input('digite a quantos Km fica de distancia o destino: '))
if km > 200:
    v = km * 0.45
else:
    v = km * 0.5
print('voce deve pagar {}R${:.2f}{}'
      .format(cor['azul'], v, cor['l']))
