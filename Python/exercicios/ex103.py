def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('='*40)
print(ficha(input('Nome do jogador: '), input('Gols do jogador: ')))
