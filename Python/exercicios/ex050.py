print('-=-' * 20)
print(' ' * 15, 'leitor de soma de par')
print('-=-' * 20)
sub = 0
d = int(input('quantos numeros irão ser digitados? '))
for c in range(0, d):
    n = int(input('digite um numero inteiro: '))
    if n % 2 == 0:
        sub = sub + n
print('o total é {}'.format(sub))
