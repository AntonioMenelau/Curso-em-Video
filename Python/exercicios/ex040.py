print('-=-'*20)
print(' '*25, '\033[37mMÉDIAS\033[m')
print('-=-'*20)
nome = str(input('digite o seu nome: '))
n1 = float(input('digite a sua \033[31mprimeira\033[m nota: '))
n2 = float(input('digite a sua \033[31msegunda\033[m nota: '))
m = (n1+n2)/2
if m < 5:
    print('{} \033[31mREPROVADO\033[m'.format(nome))
elif 6.9 > m > 5:
    print('{} \033[32mRECUPERAÇÃO\033[m'.format(nome))
elif m >= 7:
    print('{} \033[36mAPROVADO\033[m'.format(nome))
print('sua média foi \033[33m{:.1f}\033[m'.format(m))
print('bons estudos')
