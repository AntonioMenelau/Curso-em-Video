def area(a, b):
    m = a * b
    print(f'A area do seu terreno {a}x{b} é de {m}m²')


print('Controle de Terrenos\n'
      '--------------------')
area(float(input(f'LARGURA (m):')), float(input(f'COMPRIMENTO(m):')))
