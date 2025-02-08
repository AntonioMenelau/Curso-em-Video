print('-=-'*20)
print(' '*15, '\033[31mformas de pagamentos\033[m')
print('-=-'*20)
pag = float(input('digite o valor a ser pago: '))
esc = int(input('digite [ 1 ] a vista no cheque/dinheiro\n'
                '            \033[34mganha 10% de desconto\033[m\n'
                '       [ 2 ] a vista no cartão\n'
                '            \033[34mganha 5% de desconto\033[m\n'
                '       [ 3 ] parcelar em 2x no cartao\n'
                '            \033[34mpreço normal\033[m\n'
                '       [ 4 ] parcelar em 3x ou mais no cartao\n'
                '            \033[34macrescimo de 20%\033[m\n'
                '---------------------------------------------\n'
                'escolha: '))
if esc == 1:
    pag = pag * 0.9
    print('o valor a ser pago é de R${:.2f}'.format(pag))
elif esc == 2:
    pag = pag * 0.95
    print('o valor a ser pago é de R${:.2f}'.format(pag))
elif esc == 3:
    pag = pag / 2
    print('o valor a ser pago é de R${:.2f}'.format(pag))
elif esc == 4:
    vez = int(input('digite em quantas vezes quer dividir(max:12x): '))
    if vez > 2:
        pag = (pag*1.2) / vez
        print('o valor a ser pago é de R${:.2f}'.format(pag))
    else:
        print('nao é possivel fazer a compra, tente novamente.')
