print('-=-'*20)
print('  '*10, '\033[32mconversor\033[m')
print('-=-'*20)
tipo = int(input('digite [ 1 ] para binario\n'
                 '       [ 2 ] para octonal\n'
                 '       [ 3 ] para hexadecimal\n'
                 '-------------------------> '))
if 1 <= tipo <= 3:
    if tipo == 1:
        tipo = 'binario'
    elif tipo == 2:
        tipo = 'octonal'
    elif tipo == 3:
        tipo = 'hexadecimal'
    print('tipo de conversão escolhida: \033[32m{}\033[m'.format(tipo))
    n = int(input('digite o numero a ser convertido: '))
    if tipo == 'binario':
        c = bin(n)
    elif tipo == 'octonal':
        c = oct(n)
    else:
        c = hex(n)
    print('\033[32mo numero {} convertido em {} é {}\033[m'
          .format(n, tipo, c[2:]))
else:
    print('\033[1;31mERRO, NUMERO DE ESCOLHA NÃO IDENTIFICADO,'
          'TENTE NOVAMENTE\033[M')
