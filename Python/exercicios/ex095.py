jogadores = list()
jogador = dict()
gols = list()
while True:
    print('-='*20)
    jogador['nome'] = str(input('digite o nome do jogador: '))
    partidas = int(input('quantas partidas foram jogadas? '))
    for c in range(0, partidas):
        gols.append(int(input(f'quantos gols ele fez na {c+1}ª partida? ')))
        if c == 0:
            jogador['soma'] = gols[c]
        else:
            jogador['soma'] += gols[c]
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    while True:
        resp = str(input("quer continuar? [s/n] ")).lower()
        if resp in 'sn':
            break
        print('Erro, digite S ou N.')
    if resp in 'nN':
        break
print("-="*20)
print(f'{"cod":<3} {"nome":<15} {"gols":<17} {"total":<5}')
print("_"*40)
for x, c in enumerate(jogadores):
    print(f'{x:>3} {c["nome"]:<15} {c["gols"]} {c["soma"]:>7}')
while True:
    print("_" * 40)
    resp = int(input("mostrar dados de qual jogador? [999 para parar]"))
    print('_'*40)
    if resp == 999:
        break
    if resp <= len(jogadores)-1:
        for y, c in enumerate(jogadores):
            if y == resp:
                print(f'LEVANTAMENTO DO JOGADOR {c["nome"]}')
                for v, x in enumerate(c["gols"]):
                    print(f'    no {v+1}ª jogo fez {x}')
    else:
        print("codigo de jogador não encontrado! TENTE NOVAMENTE!")
print("_"*40)
print('<< FINALIZANDO >>')
