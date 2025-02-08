titulo = '\033[35mtabuada\033[m'
print('-=-' * 20)
print(f'{titulo:^60}')
print('-=-' * 20)
while True:
    n = int(input('digite o numero da tabuada'
                  '(numero negativo para parar): '))
    if n < 0:
        break
    print('-'*20)
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')
    print('-'*20)
print('programa encerrado. volte sempre!')
