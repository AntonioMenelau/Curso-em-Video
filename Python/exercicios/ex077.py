print('~' * 60)
print(f'{"analisador de vogais":^60}')
print('~' * 60)
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nna palavra {p} temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l} ', end='')
