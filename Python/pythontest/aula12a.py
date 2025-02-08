nome = str(input('digite o seu nome: '))
if nome == 'antonio':
    print('seu nome é bem top')
elif nome == 'clara':
    print('caramba, seu nome rima com banana')
elif nome == 'regiani' or nome == 'sara':
    print('seu nome é bem diferente')
else:
    print('seu nome é bem normal')
print('tenha um bom dia {}{}{}'.format('\033[33m', nome, '\033[m'))
