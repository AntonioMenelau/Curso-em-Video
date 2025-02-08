from random import randint
from time import sleep

print('-=-' * 20)
print(' ' * 25, '\033[36mJokenpo\033[m')
print('-=-' * 20)
pessoa = str(input('\033[31m=================\033[m\n'
                   'Escolha --pedra\n'
                   '        --papel\n'
                   '        --tesoura\n'
                   '\033[31m=================\033[m\n'
                   '--> ')).strip()
pessoa = pessoa.lower()
if pessoa == 'pedra' or pessoa == 'papel' or pessoa == 'tesoura':
    # ====================================================================
    computador = randint(1, 3)
    print('JOO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    # ====================================================================
    if computador == 1:
        computador = 'pedra'
    elif computador == 2:
        computador = 'papel'
    elif computador == 3:
        computador = 'tesoura'
    # ====================================================================
    if pessoa == computador:
        print('\033[33m'
              'EMPATE'
              '\033[m')
    elif pessoa == 'pedra' and computador == 'tesoura' or \
            pessoa == 'papel' and computador == 'pedra' or \
            pessoa == 'tesoura' and computador == 'papel':
        print('\033[34m'
              'VITORIA'
              '\033[m')
    else:
        print('\033[31m'
              'PERDEU'
              '\033[m')
    print('o computador escolheu \033[35m{}\033[m'.format(computador))
    # ====================================================================
else:
    print('\033[31mnão reconheço isso\n'
          'voce tem que escolher uma entre as tres alternativas\n'
          '--{}\033[31m--{}\033[31m--{}\033[31m--\n'
          'tente novamente\033[m'
          .format('\033[32m(PEDRA)\033[m',
                  '\033[32m(PAPEL)\033[m',
                  '\033[32m(TESOURA)\033[m'))
