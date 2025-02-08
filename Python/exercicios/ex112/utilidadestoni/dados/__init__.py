def leiadinheiro(msg):
    valida = False
    while not valida:
        dinheiro = str(input(msg)).replace(',', '.').strip()
        if dinheiro.isalpha() or dinheiro == '':
            print(f'\033[31mERRO, \"{dinheiro}\" é um valor invalido!\033[m')
        else:
            valida = True
            return float(dinheiro)
