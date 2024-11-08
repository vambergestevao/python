print('\033[1;37m====== DESAFIO 58 ======\033[m')

print('\033[1;33m- Estrutura de Repetição WHILE -\033[m')

from random import randint # Random Number
pc = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
player = 0
tentativa = 0
while player != pc:
    player = int(input('Qual é o seu palpite? '))
    if player < pc:
        print('Mais... Tente mais uma vez.')
    elif player > pc:
        print('Menos... Tente mais uma vez.')
    player == pc
    tentativa += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativa))
