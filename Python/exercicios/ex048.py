print('-=-'*20)
print('\033[31m'
      'soma de todos os numeros impares que sao multiplos de 3'
      '\033[m')
print('-=-'*20)
n = int(input('qual o numero maximo da soma? '))
s = 1
soma = 0
for c in range(0, n):
    if s % 3 == 1 and s % 2 == 1:
        soma = soma + s
    s = s + 1
print(soma)
