from ex115.lib.interface import *

def existeArquivo(nome):
    try:
        c = open(nome, 'rt')
        c.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nome):
    try:
        c = open(nome, 'wt+')
        c.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'O arquivo {nome} foi criado com sucesso')


def lerArquivo(nome):
    try:
        c = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in c:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        c.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        c = open(arq, 'at')
    except:
        print(f'Houve um erro ao cadastrar a pessoa {nome}')
    else:
        try:
            c.write(f'{nome};{idade}\n')
        except:
            print(f'ouve um erro ao cadastrar {nome}')
        else:
            print(f'Novo regitro de {nome} adicionado com sucesso.')
            c.close()
