titulo = ' leitor de tupla '
print('~' * 60)
print(f'{titulo:^60}')
print('~' * 60)
tupla = (int(input('digite o primeiro numero: ')),
         int(input('digite o segundo numero: ')),
         int(input('digite o terceiro numero: ')),
         int(input('digite o quarto numero: ')))
print(f'voce digitou os valores: {tupla}')
print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o numero 3 foi digitado na {tupla.index(3) + 1}ª vez')
else:
    print('nao foi digitado o numero 3')
print('foram digitados os numeros pares: ', end='')
for cont in tupla:
    if cont % 2 == 0:
        print(f'{cont} ', end='')
