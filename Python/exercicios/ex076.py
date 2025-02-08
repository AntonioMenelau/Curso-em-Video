titulo = 'LISTAGEM DE PREÇOS'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
tupla = ('Lapis', 1.75, 'borracha', 2,
         'caderno', 15.9, 'estojo', 25,
         'transferidor', 4.2, 'compasso', 9.99,
         'mochila', 120.32, 'canetas', 22.3, 'livro', 34.9)
pos = 0
while True:
    print(f'{tupla[pos]:.<31}R${tupla[pos+1]:>7.2f}')
    pos += 2
    if pos == len(tupla):
        break
print('-'*40)
