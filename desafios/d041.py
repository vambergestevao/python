print('\033[1;37m====== DESAFIO 41 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classifocação: MASTER.')
