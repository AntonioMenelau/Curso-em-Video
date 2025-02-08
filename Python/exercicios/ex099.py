from time import sleep


def maior(* num):
    if not len(num) == 0:
        print("-="*30)
        print('Analisando os valores passados... ')
        quantia = 0
        m = num[0]
        for c in num:
            print(c, end=' ')
            sleep(0.5)
            quantia += 1
            if m < c:
                m = c
        print(f'Foram informados {quantia} valores')
        print(f'O maior valor informado {m}')
    else:
        print("-="*30)
        print('Analisando os valores passados... ')
        print('foram informados 0 valores')
        print('O maior valor informado foi 0')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
