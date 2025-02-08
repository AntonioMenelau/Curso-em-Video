casa = float(input('digite o valor da casa: '))
salario = float(input('digite o valor do seu salario: '))
anos = float(input('digite quantos anos tem de prestação: '))
meses = anos*12
p = casa/meses
if p > salario*0.3:
    print('seu pedido foi negado')
else:
    print('parabens, voce pode comprar a casa')
print('o custo mensal sera de {:.2f} R$'.format(p))
