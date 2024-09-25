print('\033[1;37m====== DESAFIO 32 ======\033[m')

print('\033[1;33m- Módulos, Condições e Operadores Aritméticos -\033[m')

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
