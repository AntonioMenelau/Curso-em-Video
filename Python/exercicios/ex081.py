lista = list()
while True:
    lista.append(int(input('digite um numero: ')))
    cont = str(input('voce quer continuar? [s/n] ')).strip()[0]
    if cont in 'nN':
        pass
    break
print('=-='*20)
print(f'voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'os numeros em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
