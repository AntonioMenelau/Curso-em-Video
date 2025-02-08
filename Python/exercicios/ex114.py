import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('Não foi possivel acessar o site!')
else:
    print('Acessei o site do pudim!')
