from ex109 import moeda

num = int(input('Digite um numero: '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'Aumentando {10}%, temos {moeda.aumentar(num, 10)}')
print(f'Reduzindo {13}%, temos {moeda.diminuir(num, 13)}')
