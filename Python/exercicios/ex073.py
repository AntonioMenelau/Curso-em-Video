titulo = ' Brasileirão '
print('~~~'*20)
print(f'{titulo:-^60}')
print('~~~'*20)
times = ('corinthians', 'palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Spot Recife',
         'Ec Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atletico-GO')
print(f'lista de times: {times}')
print('~~~'*20)
print(f'os cinco primeiros sao {times[:5]}')
print('~~~'*20)
print(f'os 4 ultimos sao: {times[-4:]}')
print('~~~'*20)
print(f'os times em ordem alfabetica sao: {sorted(times)}')
print('~~~'*20)
print(f'o Chapecoense esta em {times.index("Chapecoense")+1}ª posição')
print('~~~'*20)
