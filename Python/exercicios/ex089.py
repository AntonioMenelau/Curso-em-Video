temp = []
tudo = []
while True:
    temp.append(str(input('nome: ')).strip())
    temp.append(float(input('nota 1: ')))
    temp.append(float(input('nota 2: ')))
    temp.append((temp[1]+temp[2])/2)
    tudo.append(temp[:])
    temp.clear()
    cont = str(input('quer continuar? [s/n] ')).strip()[0]
    if cont in 'nN':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":^7}')
for p, c in enumerate(tudo):
    print(f'{p:<4}{c[0]:<10}{c[3]:^7}')
print('-'*50)
while True:
    cont = int(input('voce quer ver a nota de qual aluno? '
                     '[999 imterrompe] '))
    if cont == 999:
        break
    if cont <= len(tudo) - 1:
        print(f'notas de {tudo[cont][0]} são {tudo[cont][1]} e '
              f'{tudo[cont][2]}')
    elif cont >= len(tudo):
        print('não foi encontrado essa pessoa')
    print('-'*50)
