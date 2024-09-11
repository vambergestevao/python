print('====== DESAFIO 28 ======')

from random import randint # Random Number
from time import sleep # Sleep time
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if player == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, não no {}!'.format(pc, player))
