aluno = dict()
aluno['nome'] = str(input('nome do aluno: '))
aluno['media'] = float(input('media do aluno: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'RECUPERAÇAO'
else:
    aluno['situaçao'] = 'REPROVADO'
print('-='*20)
for k, c in aluno.items():
    print(f'  - {k} é igual a {c}')
