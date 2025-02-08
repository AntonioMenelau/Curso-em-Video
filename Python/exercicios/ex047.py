print('-=-' * 20)
print(' '*20, '\033[34mnumeros pares\033[m')
print('-=-' * 20)
n = int(input('digite o intervalo a ser analisado: '))
s = 0
for c in range(0, n):
    s = s + 1
    if s % 2 == 0:
        print(s, ' ', end='')
