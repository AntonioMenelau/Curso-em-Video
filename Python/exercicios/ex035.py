cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
print('\033[4m''-=-' * 20, '\033[m')
print(cor['amarelo'], 'analisador de triangulos', cor['l'])
print('\033[4m''-=-' * 20, '\033[m')
a = float(input('digite a {}primeira{} reta: '
                .format(cor['vermelho'], cor['l'])))
b = float(input('digite a {}segunda{} reta: '
                .format(cor['verde'], cor['l'])))
c = float(input('digite a {}terceira{} reta: '
                .format(cor['azul'], cor['l'])))
if a < b+c and b < a+c and c < b+a:
    print('ele é um triangulo')
else:
    print('ele não é um triangulo')
