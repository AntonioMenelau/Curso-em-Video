matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = tres = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('digite um numero para a posiçao'
                                 f' [{l}, {c}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if maior < matriz[1][c]:
            maior = matriz[1][c]
    tres += matriz[l][2]
print('-='*20)
print(f'a soma dos numeros pares são: {par}')
print(f'a soma dos valores da terceira coluna são: {tres}')
print(f'o maior valor da segundo linha é: {maior}')
