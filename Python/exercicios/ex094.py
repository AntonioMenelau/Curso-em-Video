pessoa = {'nome': '', 'sexo': '', 'idade': ''}
pessoas = list()
media = acima = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    sair = str(input('Voce quer continuar? [s/n] ')).strip()
    if sair in 'nN':
        break
print(f'foram cadastradas {len(pessoas)} pessoas')
for c in pessoas:
    media += c['idade']
print(f'a media de idade do grupo é {media/len(pessoas)}')
print('as pessoas cadastradas foram: ', end='')
for c in pessoas:
    print(f' {c["nome"]}', end='')
print()
print('a lista das pessoas acima da media: ')
for c in pessoas:
    if c['idade'] > media/len(pessoas):
        print(f'Nome= {c["nome"]};Sexo= {c["sexo"]};Idade= {c["idade"]}')
print('<< ENCERRANDO >>')
