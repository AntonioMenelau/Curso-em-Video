print('-=-'*20)
print(' '*15, '\033[35mAnalisador de IMC\033[m')
print('-=-'*20)
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altuta em M: '))
imc = peso / (altura**2)
print('seu imc: {:.2f}'.format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso')
elif 25 > imc >= 18.5:
    print('voce esta no peso ideal')
elif 30 > imc >= 25:
    print('voce esta no sobrepeso')
elif 40 > imc >= 30:
    print('voce esta em obesidade')
elif imc >= 40:
    print('voce esta em obsidade morbida')
