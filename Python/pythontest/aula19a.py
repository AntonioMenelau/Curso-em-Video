estado = dict()
brasil = list()
for c in range(0, 3):
    estado['nome'] = str(input('nome do estado: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for c in brasil:
    print(f'o nome do estado é {c["nome"]}')
    print(f'a sigla do estado é {c["sigla"]}')
