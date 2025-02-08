print('-=-'*20)
print(' '*15, '\033[35mcaracteristicas numericas\033[m')
print('-=-'*20)
soma = termo = maior = menor = 0
stop = 's'
while stop != 'n':
    n = int(input('digite um numero: '))
    termo += 1
    soma += n
    if termo == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    stop = str(input('voce quer continuar? [s/n]')).strip().lower()[0]
print(f'a media de todos os {termo} numeros é {soma/termo}')
print(f'o maior numero digitado é {maior}')
print(f'o menor numero digitado é {menor}')
