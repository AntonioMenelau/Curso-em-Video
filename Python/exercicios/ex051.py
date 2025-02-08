print('-=-'*20)
print(' '*15, '\033[34mprogressao aritimetica\033[m')
print('-=-'*20)
n1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
print('PA = [', end='')
for c in range(0, 9):
    print('{}, '.format(n1), end='')
    n1 = n1 + r
print('{},...]'.format(n1))
