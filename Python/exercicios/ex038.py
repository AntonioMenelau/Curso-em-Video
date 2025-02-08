from time import sleep
print('-=-'*20)
print(' '*15, '\033[31mdetector de caracteristicas\033[m')
print('-=-'*20)
n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite outro numero inteiro: '))
print('PROCESSANDO ...')
sleep(3)
if n1 < n2:
    print('o primeiro numero :{}\n'
          'é \033[31mMENOR\033[m que\n'
          'o segundo numero :{}'.format(n1, n2))
elif n1 > n2:
    print('o primeiro numero :{}\n'
          'é \033[36mMAIOR\033[m que\n'
          'o segundo numero :{}'.format(n1, n2))
elif n1 == n2:
    print('o primeiro numero :{}\n'
          'é \033[7mIGUAL\033[m ao\n'
          'segundo numero : {}'.format(n1, n2))
