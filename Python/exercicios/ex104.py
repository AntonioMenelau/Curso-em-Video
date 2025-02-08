def leiaint(string):
    while True:
        x = input(string)
        if type(x) == int:
            return x
            break
        else:
            print('ERRO! Digite um numero inteiro válido.')


n = leiaint('Digite um numero: ')
print(f'O numero digitado foi: {n}')
