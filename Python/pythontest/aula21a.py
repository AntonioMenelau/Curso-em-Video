def par(num):
    """
    Analisador de numeros pares
    :param num: numero a ser analisado
    :return: retorna o valor Verdadeiro ou Falso
    Criado por Antonio Menelau
    """
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
if par(n):
    print(f'O numero {n} é Par')
else:
    print(f'O numero {n} é Impar')
help(par)
