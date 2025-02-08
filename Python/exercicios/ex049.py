print('-=-'*20)
print(' '*20, '\033[36mtabuada\033[m')
print('-=-'*20)
n = float(input('digite o numero da tabuada: '))
inicio = 1
for c in range(0, 10):
    r = n*inicio
    print('{:.1f} * {:.1f} = \033[7m{:.2f}\033[m'.format(n, inicio, r))
    inicio = inicio + 1
