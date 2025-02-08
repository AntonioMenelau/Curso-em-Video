from datetime import date
print('-=-'*20)
print(' '*15, 'analisador de idades')
print('-=-'*20)
maioridade = 0
menoridade = 0
for c in range(1, 8, 1):
    ano = int(input('em que ano a °{} pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade > 18:
        maioridade += 1
    else:
        menoridade += 1
print('ao todo tivemos {} pessoas de maior idade'.format(maioridade))
print('e tambem tivemos {} pessoas de menor idade'.format(menoridade))
