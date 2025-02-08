def voto(ano):
    """
    Analise de idade e autorização de voto
    :param ano: Ano do nascimento
    :return: Retorna autorização de voto por uma string
    Criado por Antonio Menelau
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos é: NÃO VOTA.'
    elif 18 < idade < 65:
        return f'Com {idade} anos é: VOTO OBRIGATORIO.'
    else:
        return f'Com {idade} anos é: VOTO OPCIONAL.'


print(voto(int(input('Digite o ano do seu nascimento: '))))
