numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'digite o {c+1}ª valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('=-='*20)
print(f'os valores pares digitados foram: {numeros[0]}')
print(f'os valores impares digitados foram: {numeros[1]}')
