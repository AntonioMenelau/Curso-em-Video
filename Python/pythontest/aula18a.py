galera = list()
dados = list()
totma = totme = 0
for c in range(0, 3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totma += 1
    else:
        print(f'{p[0]} é menor de idade')
        totme += 1
print(f'Temos {totma} de maioridade e {totme} de menoridade')
