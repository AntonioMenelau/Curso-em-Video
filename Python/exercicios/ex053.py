print('-=-'*20)
print(' '*15, '\033[1;31mdetector de palindromo\033[m')
print('-=-'*20)
frase = str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('essa frase é um palindromo')
else:
    print('essa frase não é um palindromo')
