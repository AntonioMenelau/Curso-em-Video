print('-=-'*20)
print(' '*20, '\033[36mfatorial\033[m')
print('-=-'*20)
n = r = int(input('digite o numero que sera fatorado: '))
print('calculando {}! = '.format(n), end='')
while n != 1:
    print('{} x '.format(n), end='')
    n -= 1
    r *= n
print('1 = {}'.format(r))
