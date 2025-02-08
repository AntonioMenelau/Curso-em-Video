cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
v = float(input('qual é a velocidade atual do seu carro: '))
if v > 80:
    print('{}MULTADO!{} voce excedeu o limite de 80Km/h'
          .format(cor['vermelho'], cor['l']))
    m = (v - 30) * 7
    print('VOCE TERA QUE PAGAR {}R${}{}'
          .format(cor['vermelho'], m, cor['l']))
print('dirija com segurança.')
