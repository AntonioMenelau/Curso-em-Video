lista = list()
par = list()
impar = list()
while True:
    n = int(input('digite um numero: '))
    lista.append(n)
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)
    esc = str(input('voce quer continuar? [s/n] ')).strip()[0]
    if esc in 'nN':
        break
print(f'a lista completa é {lista}')
print(f'a lista de pares é {par}')
print(f'a lista de impares é {impar}')
