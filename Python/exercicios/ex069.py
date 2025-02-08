titulo = '\033[32mcadastramento\033[m'
print('-=-'*20)
print(f'{titulo:^60}')
print('-=-'*20)
maioridade = homens = mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o seu sexo[f/m]: ')).lower().strip()
    if idade >= 18:
        maioridade += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulher += 1
    sair = str(input('Voce quer parar por aqui? [s/n] ')).lower().strip()
    print('-' * 40)
    if sair == 's':
        break
print(f'tem {maioridade} pessoas com mais de 18 anos')
print(f'tem {homens} homens cadastrados')
print(f'tem {mulher} mulheres com menos de 20 anos')
