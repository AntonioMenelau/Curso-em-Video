def escreva(s, cor=None):
    if cor == 'Azul':
        cor = int(46)
    elif cor == 'Vermelho':
        cor = int(41)
    else:
        cor = int(42)
    print(f'\033[{cor}m', '~' * (len(s)+2))
    print(f'  {s} ')
    print('', '~' * (len(s) + 2), '\n\033[m', end='')


def Help(f):
    escreva(f"Acessando o manual do comando '{f}' ", cor='Azul')
    print('\033[7m')
    help(f)
    print('\033[m', end='')


while True:
    escreva('Sistema de ajuda do PyHelp')
    func = str(input('Função ou Biblioteca > '))
    if func == 'FIM' or func == 'fim' or func == 'Fim':
        escreva('Ate logo', cor='Vermelho')
        break
    else:
        Help(func)
