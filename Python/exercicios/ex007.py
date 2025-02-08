aluno = str(input('digite o nome do aluno:'))
no1 = int(input('digite a primeira nota do aluno:'))
no2 = int(input('digite a segunda nota do aluno'))
cor = {'l':  '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'vermelho': '\033[31m',
       'lilas': '\033[35m',
       'cinza': '\033[37m'}
med = (no1 + no2) / 2
print('o aluno {}{}{} teve uma média de {}{}{}'
      .format(cor['verde'], aluno, cor['l'],
              cor['amarelo'], med, cor['l']))
