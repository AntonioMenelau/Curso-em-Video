print('-=-'*20)
print(' '*15, '\033[31manalisador completo\033[m')
print('-=-'*20)
n = int(input('quantas pessoas tem no grupo? '))
media = 0
hm = ''
ihm = 0
mulheres = 0
for c in range(1, n+1):
    print('----- {}ª pessoa -----'.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo[F/M]: ')).strip().lower()
    media += idade
    if sexo == 'm':
        if idade > ihm:
            hm = nome
            ihm = idade
    elif sexo == 'f':
        if idade < 20:
            mulheres += 1
print('a media de idade do grupo é de {:.2f} anos'.format(media/n))
print('o homen mais velho tem {} e seu nome é {}'.format(ihm, hm))
print('ao todo sao {} mulheres com menos de 20 anos'.format(mulheres))
