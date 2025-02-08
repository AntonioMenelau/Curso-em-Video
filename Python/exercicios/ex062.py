print('-=-'*20)
print(' '*15, '\033[35mProgressao Aritimetica\033[m')
print('-=-'*20)
termo = 0
mais = 10
total = 0
n = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
while mais != 0:
    total += mais
    print('PA=[', end='')
    while termo != total:
        print('{}'.format(n), end=',')
        n += r
        termo += 1
    print('...]')
    mais = int(input('quantos termos a mais voce quer ver? '))
print('FIM')
