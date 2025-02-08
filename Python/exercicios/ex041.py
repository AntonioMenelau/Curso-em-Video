from datetime import date
print('-=-'*20)
print(' '*15, '\033[33mclassificador de natação\033[m')
print('-=-'*20)
nome = str(input('Digite o seu nome: '))
ano = int(input('Digite o seu ano de nascimento: '))
anos = date.today().year-ano
if anos <= 9:
    print('{} esta classificado como \033[32mMIRIN\033[m'
          .format(nome))
elif 14 >= anos > 9:
    print('{} esta classificado como \033[32mINFANTIL\033[m'
          .format(nome))
elif 19 >= anos > 14:
    print('{} esta classificado como \033[32mJUNIOR\033[m'
          .format(nome))
elif 20 >= anos > 19:
    print('{} esta classificado como \033[32mSENIOR\033[m'
          .format(nome))
elif anos > 20:
    print('{} esta classificado como \033[32mMASTER\033[m'
          .format(nome))
