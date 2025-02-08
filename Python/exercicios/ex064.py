print('-=-'*20)
print(' '*20, '\033[37msomador\033[m')
print('-=-'*20)
print('para parar o somador digite 999')
n = soma = pos = 0
while n != 999:
    n = int(input('digite um numero: '))
    if n != 999:
        soma += n
        pos += 1
print('a soma desses {} numeros é {}'.format(pos, soma))
