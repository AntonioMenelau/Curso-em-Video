jogador = dict()
gols = list()
jogador['nome'] = str(input('digite o nome do jogador: '))
partidas = int(input('quantas partidas foram jogadas? '))
for c in range(0, partidas):
    gols.append(int(input(f'quantos gols ele fez na {c+1}ª partida? ')))
jogador['soma'] = sum(gols)
jogador['gols'] = gols[:]
print('-='*20)
print(jogador)
print('-='*20)
for x, c in jogador.items():
    print(f'o campo {x} tem o valor {c}')
print('-='*20)
print(f'o jogador {jogador["nome"]} jogou {partidas} partidas')
for x, c in enumerate(gols):
    print(f'    => Na partida {x+1}, fez {c} gols.')
print(f'foi um total de {jogador["soma"]} gols')
