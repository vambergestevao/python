print('\033[1;37m====== DESAFIO 45 ======\033[m')

print('\033[1;33m- Condições Aninhadas -\033[m')

from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada? '))
print('\033[1;31mJO\033[m')
sleep(1)
print('\033[1;31mKEN\033[m')
sleep(1)
print('\033[1;31mPÔ!!!\033[m')
sleep(1)
print('\033[1;37m-=-\033[m'* 9)
print('\033[1;34mComputador jogou {}\033[m'.format(itens[pc]))
print('\033[1;34mJogador jogou {}\033[m'.format(itens[player]))
print('\033[1;37m-=-\033[m' * 9)
if pc == 0: # pc jogou PEDRA
    if player == 0:
        print('\033[1;32mEMPATE!\033[m')
    elif player == 1:
        print('\033[1;32mJOGADOR VENCE!\033[m\033[m')
    elif player == 2:
        print('\033[1;32mCOMPUTADOR VENCEU!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA!\033[m')
elif pc == 1: # pc jogou PAPEL
    if player == 0:
        print('\033[1;32mCOMPUTADOR VENCE!\033[m')
    elif player == 1:
        print('\033[1;32mEMPATE!\033[m')
    elif player == 2:
        print('\033[1;32mJOGADOR VENCE!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA!\033[m')
elif pc == 2: # pc jogou TESOURA
    if player == 0:
        print('\033[1;32mJOGADOR VENCE!\033[m')
    elif player == 1:
        print('\033[1;32mCOMPUTADOR VENCE!\033[m')
    elif player == 2:
        print('\033[1;32mEMPATE!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA!\033[m')
