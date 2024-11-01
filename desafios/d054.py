print('\033[1;37m====== DESAFIO 54 ======\033[m')

print('\033[1;33m- Estrutura de Repetição FOR -\033[m')

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
