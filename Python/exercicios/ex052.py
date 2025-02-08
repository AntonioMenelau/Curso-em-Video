print('-=-'*20)
print(' '*15, '\033[31mnumeros primos\033[m')
print('-=-'*20)
n = int(input('digite um numero: '))
total = 0
print('[', end='')
for c in range(1, n+1, 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\033[m]')
print('o numero {} tem \033[36m{}\033[m divisores'.format(n, total))
if total == 2:
    print('\033[33m{}\033[m é um numero primo'.format(n))
else:
    print('\033[31m{}\033[m não é um numero primo'.format(n))
