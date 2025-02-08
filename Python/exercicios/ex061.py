print('-=-'*20)
print(' '*15, '\033[35mProgressao Aritimetica\033[m')
print('-=-'*20)
termo = 0
n = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
print('PA=[', end='')
while termo != 10:
    print('{}'.format(n), end=', ')
    n += r
    termo += 1
print('...]')
