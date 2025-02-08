from time import sleep
print('\033[31m-=-\033[m' * 20)
print(' ' * 22, '\033[32mcalculadora\033[m')
print('\033[31m-=-\033[m' * 20)
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
escolha = 0
while escolha != 5:
    escolha = int(input('escolha o operador:\n'
                        '   [ 1 ] soma\n'
                        '   [ 2 ] multiplicaçao\n'
                        '   [ 3 ] maior\n'
                        '   [ 4 ] outros numeros\n'
                        '   [ 5 ] sair do programa\n'
                        '========> '))
    print('\033[31m-=-\033[m' * 20)
    if escolha == 1:
        print('{:.0f} + {:.0f} = {:.0f}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('{:.1f} x {:.1f} = {:.1f}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('{:.1f} é maior que {:.1f}'.format(n1, n2))
        elif n1 < n2:
            print('{:.1f} é maior que {:.1f}'.format(n2, n1))
        else:
            print('eles sao iguais')
    elif escolha == 4:
        n1 = float(input('digite o primeiro numero: '))
        n2 = float(input('digite o segundo numero: '))
    elif escolha == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('eu nao reconheço esse comando,'
              ' porfavor tente novamente')
    print('\033[31m-=-\033[m' * 20)
print('fim do programa volte sempre')
