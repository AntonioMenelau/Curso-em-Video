from time import sleep
print('-=-'*20)
print(' '*15, '\033[33mcontagem regressiva\033[m')
print('-=-'*20)
start = int(input('digite [ 1 ] para começar: '))
n = 10
if start == 1:
    for c in range(0, 10):
        print(n)
        sleep(1)
        n = n-1
    print('KABOMMMMMMMM')
else:
    print('tu digitou errado, tente novamente')
