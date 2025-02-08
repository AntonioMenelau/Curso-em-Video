a = int(input('digite o 1° numero: '))
b = int(input('digite o 2° numero: '))
c = int(input('digite o 3° numero: '))
#analisando o menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#analisando o maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[36mo menor numero é o {}\033[m'.format(menor))
print('\033[4;36mo maior numero é o {}\033[m'.format(maior))
