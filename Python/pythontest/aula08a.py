import math
n = float(input('digite um numero:'))
raiz = math.sqrt(n)
print('a raiz do numero {} é {:.2f}'.format(n, math.ceil(raiz)))