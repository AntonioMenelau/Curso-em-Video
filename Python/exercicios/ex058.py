from random import randint
print('-=-'*20)
print(' '*7, '\033[33mtente adivinhar o que estou pensando\033[m')
print('-=-'*20)
pc = randint(0, 10)
pessoa = 11
tentativas = 1
while pc != pessoa:
    pessoa = int(input('digite um numero entre 0 e 10: '))
    if pc != pessoa:
        tentativas += 1
        if pc < pessoa:
            print('é menos, voce errou')
        elif pc > pessoa:
            print('é mais, voce errou')
print('voce conseguiu, o numero é {}\n'
      'voce teve {} tentativas'.format(pc, tentativas))
