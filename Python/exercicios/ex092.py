from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('nome: '))
nascimento = int(input('data de nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('data de contratação: '))
    pessoa['salario'] = float(input('salario: '))
    pessoa['aposentadoria'] = (pessoa['contratação']-nascimento)+35
print('-='*20)
print(pessoa)
for n, c in pessoa.items():
    print(f'{n} tem valor de {c}')
