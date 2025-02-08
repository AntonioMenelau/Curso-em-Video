from time import sleep


def contador(x, y, z):
    print('-='*20)
    print(f'contagem de {x} a {y} de {z} em {z}')
    sleep(1)
    if z < 0:
        z *= -1
    if z == 0:
        z = 1
    if x < y:
        print(x, end=' ')
        sleep(0.5)
        resultado = x + z
        print(f'{resultado}', end=' ')
        sleep(0.5)
        while True:
            resultado += z
            if resultado > y:
                break
            print(f'{resultado}', end=' ')
            sleep(0.5)
        print('FIM')
    else:
        print(x, end=' ')
        sleep(0.5)
        resultado = x - z
        print(f'{resultado}', end=' ')
        sleep(0.5)
        while True:
            resultado -= z
            if resultado < y:
                break
            print(f'{resultado}', end=' ')
            sleep(0.5)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('INICIO: ')), int(input('FIM: ')), int(input('PASSO: ')))
