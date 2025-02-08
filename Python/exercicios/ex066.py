titulo = '\033[31msomador\033[m'
print('-=-'*20)
print(f'{titulo:^60}')
print('-=-'*20)
s = pos = 0
while True:
    n = int(input('digite um numero (999 para o processo): '))
    if n == 999:
        break
    s += n
    pos += 1
print(f'a soma dos {pos} valores é {s}')
