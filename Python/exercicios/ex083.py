expressao = list(input('digite uma expressao: '))
lado1 = lado2 = 0
for c in expressao:
    if c == '(':
        lado1 += 1
    elif c == ')':
        lado2 += 1
if lado2 == lado1:
    print('sua expressão esta certa!')
else:
    print('sua expressão esta errada!')
