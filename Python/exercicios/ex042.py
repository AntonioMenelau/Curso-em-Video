print('-=-' * 20)
print(' ' * 15, '\033[34midentificador de triangulos\033[m')
print('-=-' * 20)
n1 = float(input('digite a primeira reta: '))
n2 = float(input('digite a segunda reta: '))
n3 = float(input('digite a terceira reta: '))
# identifica se é um triangulo
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    tig = 1
    print('Ele é um triangulo')
else:
    tig = 0
    print('Ele não é um triangulo')
# se for triangulo identifica que tipo de triangulo é
if tig == 1:
    if n1 == n2 == n3:
        print('Esse triangulo é \033[31mEQUILATERO\033[m')
    elif n1 != n2 != n3 != n1:
        print('Esse triangulo é \033[31mESCALENO\033[m')
    else:
        print('Esse triangulo é \033[31mISOSCELES\033[m')
