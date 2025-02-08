lista = list()
menor = list()
for c in range(0, 5):
    n = int(input('digite um numero: '))
    for v in lista:
        if v < n:
            menor.append(v)
    pos = len(menor)
    lista.insert(pos, n)
    menor.clear()
print(lista)
