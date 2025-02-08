print('-=-'*20)
print(' '*15, '\033[31mvalidador de questão\033[m')
print('-=-'*20)
sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = str(input('digite qual é o seu sexo: [f/m]')).lower()
    if sexo != 'm' and sexo != 'f':
        print('por favor digite novamente')
print('FIM.')
