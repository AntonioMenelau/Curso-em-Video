n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
m = (n1+n2)/2
if m <= 6:
    print('voce precisa estudar.')
else:
    print('parabens, voce foi muito bem')
print('sua média foi: {:.1f}'.format(m))
