from ex108 import moeda

num = int(input('Digite um numero: '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Aumentando {10}%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Reduzindo {13}%, temos {moeda.moeda(moeda.diminuir(num, 13))}')
