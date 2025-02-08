from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'teste.txt'
if not existeArquivo(arq):
    criaArquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if opc == 1:
        lerArquivo(arq)
    elif opc == 2:
        cabecalho('Cadastrar nova Pessoa')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        print('saindo do programa.... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opição valida\033[m')
    sleep(2)
