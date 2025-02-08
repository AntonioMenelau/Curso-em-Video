titulo = ' extenso '
print('=-='*20)
print(f'{titulo:~^60}')
print('=-='*20)
n = int(input('digite um numero entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete',
           'dezoito', 'dezenove', 'vinte')
while True:
    print('tente novamente.', end='')
    n = int(input('digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
print(f'voce digitou o numero {extenso[n]}')
