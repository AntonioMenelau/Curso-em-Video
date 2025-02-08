cont = soma = 0
while True:
    n = int(input('digite um numero: '))
    cont += 1
    if n == 999:
        print('acabou')
        break
    soma += n
print(soma)
