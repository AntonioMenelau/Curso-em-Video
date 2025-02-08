from datetime import date
print('-=-'*20)
print(' '*15, '\033[35mALISTAMENTO MILITAR\033[m')
print('-=-'*20)
nome = str(input('digite o seu nome: '))
data = int(input('digite o \033[31mano\033[m de seu nascimento: '))
ano = date.today().year
idade = ano-data
print('quem nasceu em {} tem {} anos em {}'.format(data, idade, ano))
if idade < 18:
    idade = 18-idade
    if idade > 1:
        print('{} ainda é muito jovem, espere {} anos'.format(nome, idade))
    else:
        print('{} ainda é muito jovem, espere {} ano'.format(nome, idade))
    print('voce vai se alistar em {}'.format(data+18))
elif idade == 18:
    print('{} \033[31mDEVE\033[m se alistar neste ano de {}'
          .format(nome, ano))
elif idade > 18:
    idade = idade-18
    if idade > 1:
        print('{} esta atrasado {} anos'.format(nome, idade))
    else:
        print('{} esta atrasado {} ano'.format(nome, idade))
    print('seu alistamento foi em {}'.format(data+18))
