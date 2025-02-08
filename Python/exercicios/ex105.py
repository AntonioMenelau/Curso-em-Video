def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de varios alunos
    :param n: Notas dos alunos (aceita varias)
    :param sit: Valor opcional, para ver a situação da classe (True ou False)
    :return: Retorna uma lista com todas as informações
    Criado por Antonio Menelau
    """
    lista = {'Total': len(n),
             'Maior': max(n),
             'Menor': min(n),
             'Média': sum(n) / len(n)}
    if sit:
        if lista['Média'] > 7:
            lista['Situação'] = 'Boa'
        elif 5 < lista['Média'] < 7:
            lista['Situação'] = 'Razoavel'
        elif lista['Média'] < 5:
            lista['Situação'] = 'Ruim'
    return print(lista)


notas(1, 9, 7)
help(notas)
