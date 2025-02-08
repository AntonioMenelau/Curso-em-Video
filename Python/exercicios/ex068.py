from random import randint
titulo = '\033[34mpar ou impar\033[m'
print('-=-'*20)
print(f'{titulo:^60}')
print('-=-'*20)
s = pontos = 0
while True:
    n = int(input('Diga um valor: '))
    pessoa = str(input('voce escolhe par ou impar? [p/i]')).lower().strip()
    computador = randint(0, 10)
    s = n+computador
    print(f'voce jogou {n} e o computador jogou {computador} a soma é {s}')
    if s % 2 == 0 and pessoa == 'p' or s % 2 == 1 and pessoa == 'i':
        pontos += 1
        print('voce ganhou')
    else:
        print('voce perdeu')
        break
    print('-'*20)
print(f'voce acertou {pontos} partidas')
print('-'*20)
