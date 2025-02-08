print('-=-'*20)
print(' '*15, 'sequencia de fibonacci')
print('-=-'*20)
n1 = 0
n2 = 1
r = 0
m = 1
total = 0
quantos = 2
pos = 0
while m != 0:
    m = int(input('quantos termos voce quer ver? '))
    if pos < 2:
        print('{} - {} - '.format(n1, n2), end='')
    pos += m
    while quantos != pos and quantos < pos:
        r = n1 + n2
        print('{} - '.format(r), end='')
        n1 = n2
        n2 = r
        quantos += 1
    print('...')
print('FIM')
